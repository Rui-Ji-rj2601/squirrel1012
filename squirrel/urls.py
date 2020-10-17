from django.urls import path

from django.conf.urls import url

from . import views


urlpatterns = [
        path('', views.index),
        path('<Unique_Squirrel_ID>/', views.add_a_squirrel, name='add_a_squirrel'),
        path('stats/', views.stats, name='stats'),
        ]
