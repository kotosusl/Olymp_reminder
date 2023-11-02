from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterAndLoginForm, NewProfileForm


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email', 'Undefined')
        password = request.POST.get('password', 'Undefined')
        return HttpResponse(f"Форма успешно отправлена {email} {password}")
    else:
        register_form = RegisterAndLoginForm()
        return render(request, 'register.html', {'form': register_form})


"""def reg_post(request):
    email = request.POST.get('email', 'Undefined')
    password = request.POST.get('password', 'Undefined')
    return HttpResponse(f"Форма успешно отправлена {email} {password}")"""


def log_in(request):
    if request.method == 'POST':
        email = request.POST.get('email', 'Undefined')
        password = request.POST.get('password', 'Undefined')
        return HttpResponse(f'Вы успешно вошли {email} {password}')
    else:
        login_form = RegisterAndLoginForm()
        return render(request, 'log_in.html', {'form': login_form})


"""def log_in_post(request):
    email = request.POST.get('email', 'Undefined')
    password = request.POST.get('password', 'Undefined')
    return HttpResponse('Вы успешно вошли')"""


def new_profile(request):
    if request.method == "POST":
        name = request.POST.get('name', 'Undefined')
        surname = request.POST.get('surname', 'Undefined')
        father = request.POST.get('father', 'Undefined')
        gender = request.POST.get('gender', 'Undefined')
        ages = request.POST.get('ages', 'Undefined')
        message_places = request.POST.getlist('message_places', [])
        return HttpResponse(f'Ваш профиль успешно сохранён {name} {surname} {father} {gender} {ages} {message_places}')
    else:
        new_profile_form = NewProfileForm()
        return render(request, 'new_profile.html', {'form': new_profile_form})


"""def new_profile_post(request):
    name = request.POST.get('name', 'Undefined')
    surname = request.POST.get('surname', 'Undefined')
    father = request.POST.get('father', 'Undefined')
    gender = request.POST.get('gender', 'Undefined')
    ages = request.POST.get('ages', 'Undefined')
    message_places = request.POST.getlist('message_places', [])
    return HttpResponse(f'Ваш профиль успешно сохранён {name} {message_places} {ages}')"""