from django.contrib.auth import admin
from django.urls import path

from . import views

urlpatterns = [
        path('admin/', admin.site.urls),
        path('login', views.loginPage(), name='login'),
]