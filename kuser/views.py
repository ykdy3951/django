from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import make_password
from .models import Kuser
from .forms import RegisterForm, LoginForm

# Create your views here.


def index(request):
    return render(request, 'index.html', {'email': request.session.get('user')})


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        kuser = Kuser(
            email=form.data.get('email'),
            nickname=form.data.get('nickname'),
            password=make_password(form.data.get('password')),
            level='1'
        )
        kuser.save()

        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    # 로그인이 정상적으로 될 경우
    def form_valid(self, form):
        self.request.session['user'] = form.data.get('email')

        return super().form_valid(form)


def Logout(request):
    if 'user' in request.session:
        del(request.session['user'])

    return redirect('/')
