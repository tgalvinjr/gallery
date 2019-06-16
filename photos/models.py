from django.db import models
import datetime as dt

# Create your models here.
class Editor(models.Model):
    '''
    contains details of the user uploading the pictures
    '''
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['first_name']    

    def save_editor(self):
        self.save()
    

class Location(models.Model):
    '''
    Contains the location of the image
    '''
    name = models.CharField(max_length =30)

class Category(models.Model):
    '''
    Contains the category of the pictures
    '''
    name = models.CharField(max_length =30, verbose_name = 'name')

    class Meta:
            verbose_name = "category"
            verbose_name_plural = "categories"

class Image(models.Model):
    '''
    Contains the grid of images to be uploaded
    '''
    image = models.ImageField(upload_to = 'images/', null=True)
    image_name = models.CharField(max_length =20)
    image_description = models.TextField(max_length =50)
    image_location = models.ForeignKey(Location, unique=False, blank=True)
    image_category = models.ForeignKey(Category, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)


