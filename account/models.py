from django.db import models
from django.contrib import auth

class User(auth.models.User,auth.models.PermissionsMixin):
    
    def __str__(self):
        return self.username


class AdminUser(models.Model):

    user = models.OneToOneField(
        auth.models.User, related_name='admins', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class FrontEndUser(models.Model):

    user = models.OneToOneField(
        auth.models.User, related_name='frontend', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
