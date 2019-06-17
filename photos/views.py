from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
# Create your views here.
def welcome (request):
    image = Image.objects.all()
    return render(request, 'pics.html',{'image':image})
