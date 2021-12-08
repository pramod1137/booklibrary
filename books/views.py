from django.shortcuts import render, HttpResponse
from books.models import Books,Bookauthors,Publisher



def contacts(request):
    return HttpResponse('Contacts')

def about(request):
    return HttpResponse('About')

def home(request):
    d={'name': Books.objects.all()}
    return render(request,'home.html',d)



# Create your views here.
