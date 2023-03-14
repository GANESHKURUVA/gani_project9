from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={
        'a':100,'b':200,'c':300,'d':250,
    }
    return render(request,'conditions.html',d)

def loops(request):
    d={
        'name':'nagalakshmi',
    }
    return render(request,'loop.html',d)
