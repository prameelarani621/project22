from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def topic(request):
    QLTO=Topic.objects.all()
    d={'topic':QLTO }
    return render(request,'topic.html',d)


def webpages(request):
    QLTO=WebPage.objects.all()
    d={'webpages':QLTO }
    return render(request,'webpages.html',d)


