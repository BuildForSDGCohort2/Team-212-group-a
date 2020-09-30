from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    '''
    This class will instantiate all the Profile objects and their methods
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='media/avatars', blank=True)
    bio = models.TextField()
