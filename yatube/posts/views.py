from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):    
    return HttpResponse('Главная страница')

# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()
def group_posts(request,slug):
    return HttpResponse(f'Посты групп [<slug:slug>]')