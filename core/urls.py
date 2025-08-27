from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:room_name>/', views.create_room, name='create'),
    path('join_room/<str:room_name>/', views.room_join, name='join'),
]