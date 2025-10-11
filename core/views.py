from django.shortcuts import render
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, 'core/home.html',settings.FIREBASE_CONFIG)

def create_room(request):
    return render(request, 'core/room.html')

def room_join(request, room_name):
    return render(request, 'core/join_room.html', {'room_name': room_name})