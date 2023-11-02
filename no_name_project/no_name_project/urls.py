from django.urls import path, include

urlpatterns = [
    path('hello', include('hello.urls')),
    path('reg_and_auth', include('reg_and_auth.urls')),
    path('main_app', include('main_app.urls'))
]
