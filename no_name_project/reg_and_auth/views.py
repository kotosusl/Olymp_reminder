from django.shortcuts import render
from django.http import HttpResponse


def register(request):
    return render(request, 'register.html')


def reg_post(request):
    email = request.POST.get('email', 'Undefined')
    password = request.POST.get('password', 'Undefined')
    return HttpResponse(f"Форма успешно отправлена {email} {password}")


def log_in(request):
    return render(request, 'log_in.html')


def log_in_post(request):
    email = request.POST.get('email', 'Undefined')
    password = request.POST.get('password', 'Undefined')
    return HttpResponse('Вы успешно вошли')


def new_profile(request):
    return render(request, 'new_profile.html')


def new_profile_post(request):
    name = request.POST.get('name', 'Undefined')
    surname = request.POST.get('surname', 'Undefined')
    father = request.POST.get('father', 'Undefined')
    gender = request.POST.get('gender', 'Undefined')
    ages = request.POST.get('ages', 'Undefined')
    message_places = request.POST.get('message_places', 'Undefined')
    return HttpResponse(f'Ваш профиль успешно сохранён {name} {message_places} {ages}')