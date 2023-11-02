from django.urls import path
from . import views

urlpatterns = [
    path('/register', views.register),
    path('/log_in', views.log_in),
    path('/new_profile', views.new_profile),
]