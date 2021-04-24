from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'construction/index.html')

def services(request):
    return render(request, 'construction/service.html')

def about(request):
    return render(request, 'construction/about.html')

def projects(request):
    return render(request, 'construction/project.html')

def contact(request):
    return render(request, 'construction/contact.html')

