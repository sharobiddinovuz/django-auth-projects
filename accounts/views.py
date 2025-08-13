from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from .forms import UserRegisterForm, UserLoginForm
from django.contrib import messages

# Create your views here.
def register_view(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Muvaffaqiyatli ro'yhatdan o'tdingiz!")
            return redirect(reverse_lazy('home'))
        else:
            messages.error(request, "Ro‘yxatdan o‘tishda xatolik bor. Ma’lumotlarni tekshiring.")
    else:
        form = UserRegisterForm()

    return render(request, template_name='registrations/register.html', context={'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method=="POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Xush kelibsiz!")
                return redirect('home')
            else:
                messages.error(request, "Username yoki parol xato!")
    else:
        form = UserLoginForm()

    return render(request, template_name='registrations/login.html', context={"form": form})


class CustomLogoutView(LogoutView):

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, "Hisobdan muvaffaqiyatli chiqdingiz!")
        return super().dispatch(request, *args, **kwargs)
    