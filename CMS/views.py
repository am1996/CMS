from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm

class CustomLoginview(LoginView):
    authentication_form = CustomLoginForm
    template_name = "./main/login.html"
    