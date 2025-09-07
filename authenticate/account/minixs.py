from django.shortcuts import redirect

class LogoutRequiredMinix(object):
    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(LogoutRequiredMinix, self).dispatch(*args, **kwargs)          