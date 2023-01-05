from django.shortcuts import render

# Create your views here.
def operations(request):
    d={'a':111,'b':226,'c':23}
    return render(request,'operations.html',d)
