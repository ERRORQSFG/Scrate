from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from .forms import *
from .models import *

# Create your views here.
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'crepy/reg.html'
    success_url = reverse_lazy('login')

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'crepy/login.html'

    def get_success_url(self):
        return reverse_lazy('user_page')

def register(request):
    return render(request, 'crepy/reg.html', locals())

def logout_user(request):
    logout(request)
    return redirect('/')

def user_page(request):
    return render(request, 'crepy/user.html', locals())