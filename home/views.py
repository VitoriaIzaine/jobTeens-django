from django.db.models import Q
from django.shortcuts import render, Http404, get_object_or_404



def index(request):
    return render(request, 'home/index.html')

def lei(request):
    return render(request, 'home/leiaprendiz.html')

def parceiros(request):
    return render(request, 'home/parceiros.html')

def sobre(request):
    return render(request, 'home/sobrenos.html')

def dicas(request):
    return render(request, 'home/dicas.html')






