from django.views import generic
from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy

from .forms import(
    LoginForm
)
from .minixs import(
    LogoutRequiredMinix
)

@method_decorator(never_cache, name='dispatch')
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

@method_decorator(never_cache, name='dispatch')
class Login(LogoutRequiredMinix, generic.View):
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
    
    
class Logout(generic.View):
    def get(self, *args, **kwargs):
        logout(self.request)
        return redirect('login')