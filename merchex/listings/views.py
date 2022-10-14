
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail

from listings.models import Band
from listings.models import Title
from listings.forms import BandForm, ContactUsForm


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})
    
def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request, 'listings/band_detail.html', { 'band': band })

# listings/views.py

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)

    else:
        form = BandForm()

    return render(request,
            'listings/band_create.html',
            {'form': form})

def about(request):
    return HttpResponse('<h1>A Propos</h1> <p>Nous adorons merch !</p>')

def listings(request):
    titles = Title.objects.all()
    return render(request, 'listings/listings.html', {'titles': titles})

def listing_detail(request, id):
    title = Title.objects.get(id=id)
    return render(request, 'listings/listing_detail.html', { 'title': title })

def about(request):
    return render(request, 'listings/about.html')

def contact(request):

    print('Les méthodes de requête est :', request.method)
    
    if request.method == 'POST':

        form = ContactUsForm(request.POST)



        if form.is_valid():
            print('Le formulaire est valide')

    else:
        form = ContactUsForm()

    return render(request, 
            'listings/contact.html', 
            {'form': form})