from django.http import HttpResponse
from django.shortcuts import render 
from Service.models import Service
from news.models import News

def HomePage(request):
    newsData = News.objects.all()
    Datas = {
        'newsData':newsData
    }
    
    return render(request,"index.html",Datas)

def newsDetail(request,newsid):

    return render(request,"news.html")


def contact(request):
    return render(request,"contact.html")


def product_details(request):
    return render(request,"product-details.html")


def Shop(request):
    serviceData = Service.objects.all()
    #for a in serviceData:
    #    print(a.service_title);
    data = {
        'serviceData': serviceData,
    }
    return render(request,"shop.html",data)

#def HomeCall(request,homeid):
 #   return render(request,"index.html")

