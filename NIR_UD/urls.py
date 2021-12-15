from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('about', views.about),
    re_path('^NIR_UD/$', views.auth, name='namespace'),
    path('', views.index),
    path('admin', views.admin)
]
