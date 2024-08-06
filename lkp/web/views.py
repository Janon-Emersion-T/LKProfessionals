from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request, 'web/index.html')

def about(request):
    return render (request, 'web/about.html')

def pricing(request):
    return render (request, 'web/pricing.html')

def blog(request):
    return render (request, 'web/blog.html')

def faq(request):
    return render (request, 'web/faq.html')