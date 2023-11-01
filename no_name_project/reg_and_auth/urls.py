from django.urls import path
from . import views

urlpatterns = [
    path('/register', views.register),
    path('/log_in', views.log_in),
    path('/new_profile', views.new_profile),
    path('/reg_post', views.reg_post),
    path('/log_in_post', views.log_in_post),
    path('/new_profile_post', views.new_profile_post)
]