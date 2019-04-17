from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):

    def __str__(self):
        return self.email

class Files(models.Model):
    title = models.CharField(max_length=100)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    file_name = models.FileField(upload_to='files/', max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

