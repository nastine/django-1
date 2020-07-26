from django.http import HttpResponse
from django.shortcuts import render, reverse
import pytz
from datetime import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time =  datetime.now(pytz.timezone('Europe/Moscow'))
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # file_names = []
    # for files in os.walk("app"):  
    #     for filename in files:
    #         file_names.append(filename)
    file_names = os.listdir('app')
    
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    msg = f'Содержимое рабочей директории: {file_names}'
    return HttpResponse(msg)
