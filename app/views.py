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


def Acessrecord(request):
    QLTO=AcessRecord.objects.all()
    d={'AcessRecord':QLTO}
    return render(request,'Acessrecord.html',d)


def insert_topic(request):
    tn=input('enter topic name')
    NTO=Topic.objects.get_or_create(topic_name=tn)[0]
    NTO.save()
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'topic.html',d)



def insert_WebPages(request):
    tn=input('enter topic name')
    n=input('enter name ')
    u=input('enter url name')
    TO=Topic.objects.get(topic_name=tn)
    NWO=WebPage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    NWO.save()
    QLTO=WebPage.objects.all()
    d={'WebPages':QLTO}
    return render(request,'WebPages.html',d)


def insert_AcessRecord(request):
    pk=int(input('enter pk value of webpage'))
    a=input('enter auther')
    d=input('enter date')
    WO=WebPage.objects.get(pk=pk)
    NAO=AcessRecord.objects.get_or_create(name=WO,auther=a,date=d)[0]
    NAO.save()
    QLTO=AcessRecord.objects.all()
    d={'AcessRecord':QLTO}
    return render(request,'AcessRecord.html',d)
