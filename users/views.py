from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from .forms import FilesForm
from .models import Files, CustomUser
from .forms import CustomUserCreationForm

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

def upload_file(request):
    if request.method == 'POST':
        form = FilesForm(request.POST, request.FILES)
        if form.is_valid():
            fs = form.save(commit = False)
            fs.uploader = request.user
            print(request.user)
            fs.save()
            return redirect('file_list')    
    form = FilesForm()
    return render(request, 'upload_file.html', {
        'form': form
    })