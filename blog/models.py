from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from slugify import slugify


class Categories(models.TextChoices):
    '''
    This class will instantiate all the Crop category objects and their methods
    '''
    MAIZE = "maize"
    WHEAT = "wheat"
    RICE = "rice"
    TEA = "tea"
    COFFEE = "coffee"
    FLOWERS = "flowers"
    BANANA = "banana"
    AVOCANDO = "avocando"
    COTTON = "cotton"
    CABBAGE = "cabbage"
    SUGARCANE = "sugerCane"
    OKRA = "okra"
    CARROT = "carrot"
    CUCUMBER = "cucumber"
    LETTUCE = "lettuce"
    TOMATO = "tomato"
    GROUDNUTS = "groundnuts"
    BEANS = "beans"
    ONION = "onion"
    CASSAVA = "cassava"


class Stage(models.TextChoices):
    '''
    This class will instantiate all the Stage objects and their methods
    '''
    GENERAL = "general"
    LANDPREP = "landprep"
    SEEDSELECTION = "seedselection"
    CROPCARE = "cropcare"
    HARVESTING = "harvesting"
    STORAGE = "storage"
    MARKETING = "marketing"


class Article(models.Model):
    '''
    A class that will instantiate all the Article objects and their methods
    '''
    title = models.CharField(max_length=200)
    crop = models.CharField(
        max_length=100, choices=Categories.choices, default=Categories.MAIZE)
    slug = models.SlugField(default="article")
    farmer = models.ForeignKey(User, on_delete=models.CASCADE)
    stage = models.CharField(
        max_length=100, choices=Stage.choices, default=Stage.GENERAL)
    excerpt = models.CharField(max_length=255, default="This is a simple excerpt of the blog.")
    content = models.TextField(blank=True, null=True)
    cropimage = models.ImageField(
        upload_to='cropimages/', blank=True, null=True)
    featured = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now=True, blank=True)
    update_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = Article.objects.all().filter(slug__iexact=original_slug).count()
        count = 1
        slug = original_slug
        while(queryset):
            slug = original_slug + "-"+str(count)
            count += 1
            queryset = Article.objects.all().filter(slug__iexact=slug).count()
        self.slug = slug

        if self.featured:
            try:
                featuredArticle = Article.objects.get(featured=True),
                if self != featuredArticle:
                    featuredArticle.featured = False
                    featuredArticle.save()

            except Article.DoesNotExist:
                pass
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.crop}: {self.title}'
