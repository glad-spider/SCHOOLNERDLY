from django.urls import path

# . - from this directories import
from . import views

# отслеживаем страницку пользователя
urlpatterns = [
    #путь к странице, обращение к навзванию функции которую нужно вызвать
    path('', views.index),
    path('about-us', views.about),
]
