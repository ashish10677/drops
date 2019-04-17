from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from .forms import FilesForm, CustomUserCreationForm
from .models import Files, CustomUser

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
    if request.method == "POST":
        print(request)
        return redirect('file_list')
    file_to_split = get_object_or_404(Files, pk = pk)
    return render(request, 'file_split.html', {'file_to_split': file_to_split})