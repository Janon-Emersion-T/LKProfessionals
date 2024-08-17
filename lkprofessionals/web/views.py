from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'web/index.html')

def about(request):
    return render(request, 'web/about.html')

def careers(request):
    return render(request, 'web/careers.html')

def contact(request):
    return render(request, 'web/contact.html')

def faq(request):
    return render(request, 'web/faq.html')

def features(request):
    return render(request, 'web/features.html')

def privacy_policy(request):
    return render(request, 'web/privacy-policy.html')