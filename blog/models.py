from django.db import models
from django.contrib.auth.models import User


class Crop(models.Model):
    '''
    This class will instantiate all the Crop objects and their methods
    '''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Stage(models.Model):
    '''
    This class will instantiate all the Stage objects and their methods
    '''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Article(models.Model):
    '''
    A class that will instantiate all the Article objects and their methods
    '''
    crop = models.ForeignKey(Crop,on_delete=models.CASCADE)
    farmer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    stage = models.ForeignKey(Stage,on_delete=models.CASCADE,null=True)
    content = models.TextField(blank=True, null=True)
    cropimage = models.ImageField(upload_to='media/cropimages',blank=True, null=True)

    def __str__(self):
        return f'{self.crop}: {self.title}'

