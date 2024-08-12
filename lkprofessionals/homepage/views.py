from django.shortcuts import render

def home(request):
    return render(request, 'homepage/home.html')

def about(request):
    return render(request, 'homepage/about.html')

def services(request):
    return render(request, 'homepage/services.html')

def for_individuals(request):
    return render(request, 'homepage/for_individuals.html')

def for_businesses(request):
    return render(request, 'homepage/for_businesses.html')

def pricing(request):
    return render(request, 'homepage/pricing.html')

def contact(request):
    return render(request, 'homepage/contact.html')
