from django.urls import path

# . - from this directories import
from . import views

# отслеживаем страницку пользователя
urlpatterns = [
    #путь к странице, обращение к навзванию функции которую нужно вызвать
    # name-"" - > это для того что бы легче обращаться к ссылке страницы в html файле
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('create', views.create, name='create'),
]
