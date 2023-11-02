from django.urls import path
from . import views

urlpatterns = [
    path('/main', views.main_window),
    path('/profile', views.profile_window),
    path('/messages', views.message_window),
]
