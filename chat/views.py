from django.views.generic import TemplateView, DeleteView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ChatRoom, Message
from datetime import datetime
# from time import strftime


def index(context):
    return render(context, 'index.html')


@login_required
def chat(request):
    room_names = ChatRoom.objects.all()
    return render(request, "chat/chat.html", {"room_names": room_names})


@login_required
def room(request, slug):
    room = ""
    messages = ""
    try:
        time = datetime.now()
        room_names = ChatRoom.objects.all()
        room = ChatRoom.objects.get(slug=slug)

        messages = Message.objects.filter(room=room)[0:25]
    except:
        name = slug.title()
        ChatRoom.objects.create(name=name, slug=slug)



    return render(request, "chat/room.html", {"room_names": room_names, "room": room, "time": time, "messages": messages})

