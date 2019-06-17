from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Image
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def welcome(request):
    image = Image.objects.all()
    return render(request, 'pics.html', {'image': image})

def single_image(request, image_id):
    try:
        image = Image.objects.filter(id=image_id)
    except ObjectDoesNotExist:
        raise Http404()

    return render(request, "imgdetails.html", {"image": image})
