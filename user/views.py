from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm
# Create your views here.

def login_view(request):
    if request.user.is_authenticated == False:
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')

        return render(request, "user/loginform.html", {"form": form,'title':'Giriş Yap',})
    else:
        return redirect('home')

def logout_view(request):

    if request.user.is_authenticated:
        logout(request)
        return redirect('home')
    else:
        return redirect('401')

def accounts_view(request):

    context = {}

    return render(request,'user/hesap.html',context)
