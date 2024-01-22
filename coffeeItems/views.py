from django.shortcuts import render
from django.http import HttpResponse
from .models import Coffee,Premium,Question

# Create your views here.
def Home(request):
  coffee=Coffee.objects.all()
  return render(request,'home.html',{'coffee':coffee})

def Pricing(request):
  premium=Premium.objects.all()
  return render(request,'Pricing.html',{'premium':premium})


def SignIn(request):
  return render(request,'register.html')


def LogIn(request):
  return render(request,'login.html')

def FrequentlyAskedQuestion(request):
  questions=Question.objects.all()
  return render(request,'FAQs.html',{'questions':questions})

def AboutUs(request):
  return render(request,'AboutUs.html')