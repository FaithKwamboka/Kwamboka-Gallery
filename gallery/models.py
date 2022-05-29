from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
class categories(models.Model):
    category=models.CharField(max_length=40)
    
    def save_category(self):
        self.save()
        
    def delete_category(self):
        self.delete()
    
    class Meta:
        verbose_name_plural = ('categories')

    def __str__(self):
        return self.category

class Location(models.Model):
    location=models.CharField(max_length=40)
    
    def save_location(self):
        self.save()
        
    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.location
    

class Image(models.Model):
    name= models.CharField(max_length=50)
    description = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)
    gallery_image = models.ImageField(upload_to='uploads/', blank=True, default='image')
    categories = models.ManyToManyField(categories)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    
    
    class Meta:
        ordering = ('posted',)
        
    def save_image(self):
            self.save()
        
    def delete_image(self):
        self.delete()
        
    def __str__(self):
        return self.name

    @classmethod
    def all_images(self):

        return Image.objects.all()

    @classmethod
    def search_by_category(cls,search_images):
        images = Image.objects.filter(categories__category__icontains=search_images)
        return images

    @classmethod
    def view_location(cls,location):
        location = cls.objects.filter(location=location)
        return location

    @classmethod
    def view_category(cls,cate):
        categories = cls.objects.filter(categories=cate)
        return categories
    
    
    
   