from django.views import generic
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy

from .forms import(
    LoginForm
)


class Index(LoginRequiredMixin,generic.TemplateView):
    login_url = reverse_lazy("login")
    template_name = "shope/index.html"
    
    
class About(generic.TemplateView):
    template_name = "shope/about.html"

class Contact(generic.TemplateView):
    template_name = "shope/contact.html"
    
class Price(generic.TemplateView):
    template_name = "shope/price.html"

class Hours(generic.TemplateView):
    template_name = "shope/hours.html"    

class Login(generic.View):
    def get(self, *args, **kwargs):
        form = LoginForm()
        context = {
            "form":form
        }
        return render(self.request, 'account/login.html', context)
    
    def post(self,*args,**kwargs):
        form = LoginForm(self.request.POST)
        if form.is_valid():
            user = authenticate(
                self.request,
                username = form.cleaned_data.get("username"),
                password = form.cleaned_data.get("password")
            )
            if user:
                login(self.request, user)
                return redirect('home')
            else:
                messages.warning(self.request, "Wrong Credentials")
                return redirect('login')
        return render(self.request, 'account/login.html', {"form":form})