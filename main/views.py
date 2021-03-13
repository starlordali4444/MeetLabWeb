from django.shortcuts import render

def index(request):
    context={
        "n":1
    }  
    return render(request,"main/index.html",context=context)

def contact(request):
    context={
        "title":"Contact Us",
    }
    return render(request,"main/contact.html", context=context)
