
from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Title


def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', {'bands': bands})
    

def about(request):
    return HttpResponse('<h1>A Propos</h1> <p>Nous adorons merch !</p>')

def listings(request):
    titles = Title.objects.all()
    return render(request, 'listings/listings.html', {'titles': titles})
def contact(request):
    return HttpResponse('<h1>Contact</h1> <p>Nous contacter</p>')