from django.shortcuts import render

from .models import Worker

# Create your views here.

def index_page(request):
    all_users = Worker.objects.all()
    return render(request, '../templates/myapp1/index.html', context={'users': all_users})


def index_page1(requst):
    return render(requst, '../templates/myapp1/index.html')


def generic_page(request):
    return render(request, '../templates/myapp1/generic.html')


def elements_page(request):
    return render(request, '../templates/myapp1/elements.html')