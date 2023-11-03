from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegisterAndLoginForm, NewProfileForm


def register(request):
    if request.method == 'POST':
        user_form = RegisterAndLoginForm(request.POST)
        if user_form.is_valid():
            email = user_form.cleaned_data['email']
            password = user_form.cleaned_data['password']
            return HttpResponseRedirect('/reg_and_auth/new_profile')
        else:
            return render(request, 'register.html', {'form': user_form})
    else:
        register_form = RegisterAndLoginForm()
        return render(request, 'register.html', {'form': register_form})


"""def reg_post(request):
    email = request.POST.get('email', 'Undefined')
    password = request.POST.get('password', 'Undefined')
    return HttpResponse(f"Форма успешно отправлена {email} {password}")"""


def log_in(request):
    if request.method == 'POST':
        user_form = RegisterAndLoginForm(request.POST)
        if user_form.is_valid():
            email = user_form.cleaned_data['email']
            password = user_form.cleaned_data['password']
            return HttpResponseRedirect('/main_app/main')
        else:
            return render(request, 'log_in.html', {'form': user_form})
    else:
        login_form = RegisterAndLoginForm()
        return render(request, 'log_in.html', {'form': login_form})


"""def log_in_post(request):
    email = request.POST.get('email', 'Undefined')
    password = request.POST.get('password', 'Undefined')
    return HttpResponse('Вы успешно вошли')"""


def new_profile(request):
    if request.method == "POST":
        user_form = NewProfileForm(request.POST)
        if user_form.is_valid():
            name = user_form.cleaned_data['name']
            surname = user_form.cleaned_data['surname']
            father = user_form.cleaned_data['father']
            gender = user_form.cleaned_data['gender']
            ages = user_form.cleaned_data['ages']
            message_places = request.POST.getlist('message_places', [])
            # return HttpResponseRedirect('/main_app/main')
            return HttpResponse(f'Ваш профиль успешно сохранён {name} {surname} {father} {gender} {ages} {message_places}')
        else:
            return render(request, 'new_profile.html', {'form': user_form})
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