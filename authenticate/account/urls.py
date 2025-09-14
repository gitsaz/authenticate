from django.urls import path

from .views  import(
    Index,
    About,
    Contact,
    Price,
    Hours,
    Login,
    Logout,
    Registration,
    ChangePassword,
)

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('contact/', Contact.as_view(), name='contact'),
    path('price/', Price.as_view(), name='price'),
    path('hours/', Hours.as_view(), name='hours'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('registration/', Registration.as_view(), name='registration'),
    path('change_password/', ChangePassword.as_view(), name="change_password")
    
]

