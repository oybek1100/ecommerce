from django.shortcuts import render
from django.contrib.auth.views import LoginView 
from .models import MyUser
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import CreateView 
from .forms import CustomUserCreationForm


class CustomLoginView(LoginView):
    model = MyUser
    template_name = 'users/login.html'
    fields = ('username' , 'password')
    success_url = reverse_lazy('ecommerce:index')

class CustomRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('ecommerce:index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
