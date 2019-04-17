from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from .forms import FilesForm, CustomUserCreationForm
from .models import Files, CustomUser
from django.conf import settings
from .split import split_file

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def file_list(request):
    current_user = CustomUser.objects.get(email = request.user)
    files = Files.objects.filter(uploader = current_user)
    return render(request, 'file_list.html', {
        'files': files
    })

def file_upload(request):
    if request.method == 'POST':
        form = FilesForm(request.POST, request.FILES)
        if form.is_valid():
            fs = form.save(commit = False)
            fs.uploader = request.user
            fs.save()
            return redirect('file_list')    
    form = FilesForm()
    return render(request, 'file_upload.html', {
        'form': form
    })

def file_split(request, pk):
    file_to_split = get_object_or_404(Files, pk = pk)
    if request.method == "POST":
        path = str(settings.MEDIA_ROOT)+"/"+str(file_to_split.file_name)
        split_file(path, 5)
        return redirect('file_list')
    return render(request, 'file_split.html', {'file_to_split': file_to_split})