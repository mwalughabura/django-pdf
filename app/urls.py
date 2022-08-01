from django.urls import path
from . import views

"""
I hope this works
"""
urlpatterns = [
    path('', views.index, name='index'),

    path('certificate', views.certificate),
]