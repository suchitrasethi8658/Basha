from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse

# Create your views here.
def suchi(request):
    s=SuchiForm()
    d={'form':s}
    if request.method=='POST':
        S=SuchiForm(request.POST)
        if S.is_valid():
            S.save()
        return HttpResponse('Submitted')

    return render(request,'suchi.html',d)
def basha(request):
    b=BashaForm()
    d={'form':b}
    if request.method=='POST':
        B=BashaForm(request.POST)
        if B.is_valid():
            B.save()
        return HttpResponse('Submitted')
    return render(request,'basha.html',d)