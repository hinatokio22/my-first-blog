from django.shortcuts import render
from codemath.forms import convertform
from django.http import HttpResponse
# Create your views here.

def index(request):
    #mostrame=convertir.objects.all()
    return render(request, 'blog/index.html', {})

def ecuaciones(request):
    return render(request,'blog/ecuaciones.html',{} )
    #return HttpResponse("donde estoy")
def integrales(request):
    return render(request,'blog/integrales.html',{} )
