from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')

def busmap(request):
    return render(request, 'myapp/busmap.html')