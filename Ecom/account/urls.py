from . import views
from django.urls import path

urlpatterns = [
    path('register/',views.accountLogin, name="register"),
    path('login/', views.Login, name='login')
]