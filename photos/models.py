from django.db import models

# Create your models here.
class Editor(models.Model):
    '''
    Editor model to show the user who is to upload the pictures
    '''
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)