from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('files/', views.file_list, name="file_list"),
    path('files/upload', views.upload_file, name='file_upload'),
]