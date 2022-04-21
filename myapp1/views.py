from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def funct1(request):
    return HttpResponse('Sample text')
def funct2(request):
    return render(request,'myproject.html')