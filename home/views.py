from django.db.models import Q
from django.shortcuts import render, Http404, get_object_or_404



def index(request):
    return render(request, 'home/index.html')

def leiaprendiz(request):
    return render(request, 'home/leiaprendiz.html')





