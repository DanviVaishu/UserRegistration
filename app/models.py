from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
    profile_user=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.TextField()
    profile_pic=models.ImageField()