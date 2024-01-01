from django.shortcuts import render,redirect
from .forms import RegiserForm,LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout

# Create your views here.
def Register(request):
    if request.method == "POST":
        form = RegiserForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            newuser = User(username=username)
            newuser.set_password(password)
            newuser.save()
            login(request,newuser)
            messages.success(request, "Kayıt İşlemi  Başarılı")
            return redirect("index")
        else:
            context = {"form": form,}
            return render(request, "register.html", context)
    else:
        form = RegiserForm()
    context = {"form": form,}
    return render(request, "register.html", context)
def Login(request):
    if request.method == "POST":
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            
            if user is None:
                context = {"form": form,}
                messages.error(request, "Kullanıcı Adı yada Parola Hatalı")
                return render(request, "login.html", context)
            else:
                messages.success(request, "Başarıyla Giriş Yaptınız...")
                login(request,user)
                return redirect("index")
            
        else:
            context = {"form": form,}
            return render(request, "login.html", context) 
    else:
        form = LoginForm()
        context = {
            "form":form
        }
        return render(request, "login.html",context)
def Logout(request):
    logout(request)
    messages.success(request, "Başarıyla Çıkış Yaptınız...")
    return redirect("index")