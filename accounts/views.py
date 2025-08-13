from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from .forms import UserRegisterForm, UserLoginForm
from django.views.generic import CreateView, FormView
from django.contrib import messages

# Create your views here.
class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "registrations/register.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        messages.success(self.request, "Muvaffaqiyatli ro'yhatdan o'tdingiz!")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Ma'lumotlarni tekshirib qayta kiriting!")
        return super().form_invalid(form)

class UserLoginView(FormView):
    form_class = UserLoginForm
    template_name = "registrations/login.html"
    success_url = reverse_lazy('home')
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.get_success_url())
        return super().get(request, *args, **kwargs)

    def form_valid(self, form): 
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            messages.success(self.request, "Xush kelibsiz!")
            return super().form_valid(form)
        else:
            messages.error(self.request, "Username yoki parol xato!")
            return super().form_invalid(form)
    

    def form_invalid(self, form):
        messages.error(self.request, "Formada xatolik bor qayta tekshirib ko'ring!")
        return super().form_invalid(form)


class CustomLogoutView(LogoutView):

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, "Hisobdan muvaffaqiyatli chiqdingiz!")
        return super().dispatch(request, *args, **kwargs)
    