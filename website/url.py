from django.urls import path

from . import views

app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'),
    path('event/create/', views.event_create, name='event_create')
]