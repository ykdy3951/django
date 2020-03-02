from django.shortcuts import redirect
from .models import Kuser


def login_required(function):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/login')
        return function(request, *args, **kwargs)

    return wrap


def admin_required(function):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/login')

        user = Kuser.objects.get(email=user)
        if int(user.level) < 2:
            return redirect('/')

        return function(request, *args, **kwargs)
    return wrap
