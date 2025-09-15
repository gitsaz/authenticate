import re
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import(
    PasswordResetForm
    
)
    
from .models import(
    Message
)

User = get_user_model()


class LoginForm(forms.Form):
    # দিলে → আপনি ফর্ম তৈরির সময় নিজের কাস্টম কাজ করতে পারবেন।
    # যেমনঃ প্রতিটি ফিল্ডে class="form-control" বসানো, placeholder দেওয়া, label বদলানো ইত্যাদি।
    # না দিলে → Django ডিফল্ট Form এর constructor চলবে। ফর্ম ঠিকই কাজ করবে, কিন্তু আপনার extra styling বা পরিবর্তন হবে না।
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #ei loop tar kaj holo form control newa. mane form er username password field er style er control newa. ei same kaj tai niche kora holo.
        
        # for field in self.fields:
        #     self.fields[field].widget.attrs.update({"class":"form-control"})
        
    username =forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={"class":"form-control"})
    )
    password = forms.CharField(
        max_length=150,
        widget= forms.PasswordInput(attrs={"class":"form-control"})
    )


class UserRegistrationForm(forms.ModelForm):
    
    password = forms.CharField(
        max_length=150,
        widget= forms.PasswordInput(attrs={"class":"form-control"})
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            "username": forms.TextInput(attrs={"class":"form-control"}),
            "email": forms.EmailInput(attrs={"class":"form-control"}),
        }
     
    #1.duplicate username check    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError("This username already taken")
        return username
        
    #2.duplicate email check
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("This email already taken")
        return email
        
    def clean_password(self, *args, **kwargs):
        password = self.cleaned_data.get('password')
        password2 = self.data.get('password2')
        
        #1.password match check
        if password != password2:
            raise forms.ValidationError("Password do not match")
        #2. password length check   
        if password and len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long")
        #3.password must contain at lest one special character
        if password and not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            raise forms.ValidationError("Password must contain at least one special character (!@#$%^&*)")
        return password
        
    def save(self, commit = True ,*args, **kwargs):
        user = self.instance
        user.set_password(self.cleaned_data.get('password'))
        
        if commit:
            user.save()
        return user
    
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('name', 'email', 'message')
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={"class": "form-control"}),
        }
    def clean_email(self):
            email = self.cleaned_data.get('email')
            if not User.objects.filter(email=email).exists():
                raise forms.ValidationError("This email is not registered")
            return email
        
        
class ChangePasswordForm(forms.Form):
    
    current_password =forms.CharField(
        max_length=150,
        widget=forms.PasswordInput(attrs={"class":"form-control"})
    )
    new_password1 =forms.CharField(
        max_length=150,
        widget=forms.PasswordInput(attrs={"class":"form-control"})
    )
    new_password2 =forms.CharField(
        max_length=150,
        widget=forms.PasswordInput(attrs={"class":"form-control"})
    )
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)
        
    def clean_current_password(self, *args, **kwargs):
        current_password = self.cleaned_data.get('current_password')
        
        if not self.user.check_password(current_password):
            raise forms.ValidationError('Incorrect |Password')    
    
    def clean_new_password1(self, *args, **kwargs):
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.data.get('new_password2')
        
        
        if new_password1 != new_password2:
            raise forms.ValidationError('Password do not match')
        #1. password length check   
        if new_password1 and len(new_password1) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long")
        #2.password must contain at lest one special character
        if new_password1 and not re.search(r"[!@#$%^&*(),.?\":{}|<>]", new_password1):
            raise forms.ValidationError("Password must contain at least one special character (!@#$%^&*)")
        
        return new_password1
    
    
class ResetPasswordForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # add bootstrap class to all fields
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class":"form-control"})
            
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("The email is not registered")
        return email

            
    def send_mail(self, subject_template_name, email_template_name, context, from_email, to_email, html_email_template_name = ...):
        return super().send_mail(subject_template_name, email_template_name, context, from_email, to_email, html_email_template_name)
        

class PasswordResetConfirmForm(forms.Form):
    new_password1 =forms.CharField(
        max_length=150,  
        widget=forms.PasswordInput(attrs={"class":"form-control"})
    )
    new_password2 =forms.CharField(
        max_length=150,
        widget=forms.PasswordInput(attrs={"class":"form-control"})
    )
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)
        
    
    def clean_new_password1(self, *args, **kwargs):
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.data.get('new_password2')
        
        
        if new_password1 != new_password2:
            raise forms.ValidationError('Password do not match')
        #1. password length check   
        if new_password1 and len(new_password1) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long")
        #2.password must contain at lest one special character
        if new_password1 and not re.search(r"[!@#$%^&*(),.?\":{}|<>]", new_password1):
            raise forms.ValidationError("Password must contain at least one special character (!@#$%^&*)")
        
        return new_password1
    
    def save(self, commit=True, *args, **kwargs):
        self.user.set_password(self.cleaned_data.get('new_password1'))
        
        if commit:
            self.user.save()
        return self.user