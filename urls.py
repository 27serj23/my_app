from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('page1/', views.page1, name='page1'),
    path('page2/', views.page2, name='page2')
]