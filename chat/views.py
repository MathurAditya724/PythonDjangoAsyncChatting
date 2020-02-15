from django.shortcuts import render, redirect, reverse
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
import json
from django.contrib.auth.models import User
from .models import Friend
from django.contrib.auth.views import LoginView


class NewLogin(LoginView):
    template_name = 'chat/index.html'

    def get_success_url(self):
        return reverse('room_list', args=[self.request.user.username])


def index(request):
    return render(request, 'chat/index.html')


@login_required
def room_list(request, user):
    user = User.objects.filter(username=user).first()
    a = Friend.objects.filter(friend_one=user)
    b = Friend.objects.filter(friend_two=user)
    return render(request, 'chat/room_list.html', {'a': a, 'b': b})


@login_required
def room(request, room_name, user):
    _user = User.objects.filter(username=user).first()
    friend = Friend.objects.filter(slug=room_name).first()
    if friend.friend_one == _user:
        other = friend.friend_two
    else:
        other = friend.friend_one

    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'sender': user,
        'other': other
    })
