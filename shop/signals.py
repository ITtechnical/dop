
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth import user_logged_in
from django.dispatch.dispatcher import receiver
from .models import  UserSession
from django.shortcuts import redirect

from .import models
from django.contrib.sessions.models import Session
from .import views


@receiver(user_logged_in)
def remove_other_sessions(sender, user, request, **kwargs):
    # remove other sessions
    Session.objects.filter(usersession__user=user).delete()

    # save current session
    request.session.save()

    # create a link from the user to the current session (for later removal)
    UserSession.objects.get_or_create(
        user=user,
        session=Session.objects.get(pk=request.session.session_key)
    )
    return redirect('login')
