from django.contrib import admin
from django.urls import path, include

# отслеживаем страницку пользователя
"""
    '' - означает что мы переходим на главную стнраницу
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'))
]
