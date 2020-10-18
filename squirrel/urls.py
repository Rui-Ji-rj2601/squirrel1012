from django.urls import path

from django.conf.urls import url

from . import views


urlpatterns = [
        path('', views.index),
        path('stats/', views.stats, name='stats'),
        path('add/', views.add, name='add'),
        path('<squirrel_id>/', views.update, name='update'),
        ]
