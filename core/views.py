from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def create_room(request, room_name):
    return render(request, 'core/room.html', {'room_name': room_name})

def room_join(request, room_name):
    return render(request, 'core/join_room.html', {'room_name': room_name})