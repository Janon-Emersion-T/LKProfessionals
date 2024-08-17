from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, 'dashboard/register.html')

def login(request):
    return render(request, 'dashboard/login.html')

def dashboard(request):
    return render(request, 'dashboard/index.html')