from django.urls import path

from django.contrib.auth.views import(
    PasswordResetDoneView,
    PasswordResetCompleteView
)

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
    PasswordReset,
    PasswordResetConfirm

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
    path('change_password/', ChangePassword.as_view(), name="change_password"),
    path('password_reset/', PasswordReset.as_view(), name="password_reset"),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name = 'account/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name="password_reset_confirm"),
    path('reset/done/', PasswordResetCompleteView.as_view(), name="password_reset_complete")
    
]

