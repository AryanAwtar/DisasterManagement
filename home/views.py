from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")
    #return HttpResponse("This is Rahul")
def contact(request):
    context={
        "variable":"this is rahul number 914285779"
    }
    return render(request, "contact.html",context)
   # return HttpResponse("This is Rahul ka contact")
def about(request):
    return render(request, "about.html")
    #return HttpResponse("This is Rahul ka about")
def services(request):
    return render(request, "services.html")
   # return HttpResponse("This is Rahul ka services")
