from django.shortcuts import render
from .models import Room



#rooms = [
 #   {'id' :1, 'name' : 'KULÜPLER'},
  #  {'id' :2, 'name' : 'ADMİNLER'},
   # {'id' :3, 'name' : 'SEN DE KATIL!'},
#]


def home(request):
    rooms = Room.objects.all()
    context = {'rooms' : rooms}
    return render(request, 'base/home.html', {'rooms':rooms})

def room(request, pk):
    room = Room.objects.get(id=pk)
    
    context = {'room': room}
    return render(request, 'base/room.html')

# Create your views here.
