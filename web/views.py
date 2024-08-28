from django.shortcuts import render

def home(request):
    return render(request, 'web/index.html')

def about(request):
    return render(request, 'web/about.html')

def services(request):
    return render(request, 'web/services.html')

def careers(request):
    return render(request, 'web/careers.html')

def contact(request):
    return render(request, 'web/contact.html')

def privacy_policy(request):
    return render(request, 'web/privacy-policy.html')

def features(request):
    return render(request, 'web/features.html')

def faq(request):
    return render(request, 'web/faq.html')