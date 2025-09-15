from django.views import generic
from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import(
    PasswordResetView,
    PasswordResetConfirmView
)
from .forms import(
    LoginForm,
    UserRegistrationForm,
    MessageForm,
    ChangePasswordForm,
    ResetPasswordForm,
    PasswordResetConfirmForm
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
    
@method_decorator(never_cache, name='dispatch')
class Registration(LogoutRequiredMinix, generic.CreateView):
    template_name = 'account/register.html'
    form_class =UserRegistrationForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        messages.success(self.request, "Registration Successful !")
        return super().form_valid(form)
    
    
class Contact(generic.FormView):
    template_name = "shope/contact.html"
    form_class = MessageForm
    success_url = reverse_lazy('contact')   # submit হওয়ার পর আবার contact পেজে redirect করবে

    def form_valid(self, form):
        form.save()  # ডাটাবেজে message সেভ হবে
        messages.success(self.request, "Your message has been sent !")
        return super().form_valid(form)
        
        
# Change Password
@method_decorator(never_cache, name='dispatch')
class ChangePassword(LoginRequiredMixin, generic.FormView):
    template_name = 'account/change_password.html'
    form_class =  ChangePasswordForm
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('login')
    
    def get_form_kwargs(self):
        context = super().get_form_kwargs()
        context['user'] = self.request.user #current password check korar jonno
        return context
    
    def form_valid(self, form):
        user = self.request.user
        user.set_password(form.cleaned_data.get('new_password1'))
        user.save()
        messages.success(self.request, 'Password Change Successfully')
        return super().form_valid(form)
    
 
@method_decorator(never_cache, name='dispatch')   
class PasswordReset(PasswordResetView):
    template_name = "account/password_reset.html"
    form_class = ResetPasswordForm
    
    
class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = "account/password_reset_confirm.html"
    form_class = PasswordResetConfirmForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        messages.success(self.request, "Password REset Successful !")
        return super().form_valid(form)