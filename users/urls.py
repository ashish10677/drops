from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('', views.file_list, name="file_list"),
    path('files/upload', views.file_upload, name='file_upload'),
    path('files/split/<int:pk>/', views.file_split, name='file_split')
]