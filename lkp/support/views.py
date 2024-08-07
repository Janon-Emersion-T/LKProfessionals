from django.shortcuts import render

# Create your views here.
def privacy(request):
    return render (request, 'support/privacy.html')

def terms_of_service(request):
    return render (request, 'support/terms_of_service.html')

def cookie_policy(request):
    return render (request, 'support/cookie_policy.html')

def right_of_withdrawal(request):
    return render (request, 'support/right_of_withdrawal.html')