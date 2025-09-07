from django.urls import path

from .views  import(
    Index,
    About,
    Contact,
    Price,
    Hours,
    Login
)

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('contact/', Contact.as_view(), name='contact'),
    path('price/', Price.as_view(), name='price'),
    path('hours/', Hours.as_view(), name='hours'),
    path('login/', Login.as_view(), name='login'),
    
]

