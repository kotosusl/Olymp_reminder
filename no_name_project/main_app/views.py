from django.shortcuts import render


def main_window(request):
    return render(request, 'main_window.html')


def profile_window(request):
    return render(request, 'profile_window.html')


def message_window(request):
    return render(request, 'message_window.html')
