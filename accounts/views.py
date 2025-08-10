from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm
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
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Xush kelibsiz!")
            return redirect('home')
        else:
            messages.error(request, "Username yoki parol xato!")

    return render(request, template_name='registrations/login.html')


def logout_view(request):
    logout(request)
    messages.info(request, "Hisobdan muvaffaqiyatli chiqdingiz!")
    return redirect('accounts:register')