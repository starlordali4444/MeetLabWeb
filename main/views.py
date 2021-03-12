from django.shortcuts import render

def index(request):
    context={
        "n":1
    }      

    return render(request,"main/index.html",context=context)
