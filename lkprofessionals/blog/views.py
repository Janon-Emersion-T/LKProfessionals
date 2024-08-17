from django.shortcuts import render


def blog(request):
    return render(request, 'web/blog.html')

def blog_single(request):
    return render(request, 'web/blog-single.html')