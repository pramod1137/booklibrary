from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

def logout_view(request):
    logout(request)
    return HttpResponse("You have successfully logged out")
def protect_view1(request) :
    if request.user.is_authenticated :
        return HttpResponse("Everything is good you can access this page")
    else :
        return HttpResponse("Login is required to view this page")

@login_required(login_url="/account/login")

def protect_view2(request) :
    return HttpResponse("you can access this page")




def login_view(request):
    next_page=request.GET.get(next)

    d={"is_login" : False}
    if request.method == "POST":
        u=request.POST["username"]
        p=request.POST["password"]
        user=authenticate(username=u,passoword=p)
        if user is not None:
            d["is login":True]
            if next_page:
                return (next_page)
            return render(request,"login.html",d)
        else :
            return render(request,"login.html",d)
    return render(request,"login.html",d)

def register_view(request) :
    d = {"is_signup": False, "error": False}
    if request.method== "POST" :
        u=request.POST["username"]
        p=request.POST["password"]
        fn=request.POST["fn"]
        ln=request.POST["ln"]
        try :
            u=User.objects.create_user(username=u, password=p, first_name=fn, last_name=ln)
            u.save()
            d["is_signup"]=True
            return render(request,"signup.html",d)
        except:
            d["error"]=True
            return render(request, "signup.html", d)

    return render(request, "signup.html", d)










        


# Create your views here.
