from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
        path('admin/', admin.site.urls),
        path('login', views.loginPage, name='login'),
        path('logout', views.logoutUser, name='logout'),
]