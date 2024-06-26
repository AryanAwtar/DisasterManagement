from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from home.form import signupform


# Create your views here.
def index(request):
    return render(request, "index.html")
    # return HttpResponse("This is Rahul")

def next(request):
    return render(request, "next.html")
    # return HttpResponse("This is Rahul")


def contact(request):
    context = {
        "variable": "this is rahul number 914285779"
    }
    return render(request, "contact.html", context)


# return HttpResponse("This is Rahul ka contact")
def about(request):
    return render(request, "about.html")
    # return HttpResponse("This is Rahul ka about")


def services(request):
    return render(request, "services.html")


# return HttpResponse("This is Rahul ka services")
def signup(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')
    else:
        form = signupform()
    return render(request, "signup.html", {'form': form})


# return HttpResponse("This is Rahul ka services")
def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('next')
    else:
        return render(request, "login.html")
# return HttpResponse("This is Rahul ka services")
