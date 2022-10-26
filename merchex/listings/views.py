
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail

from listings.models import Band
from listings.models import Title
from listings.forms import BandForm, ContactUsForm, TitleForm


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})
    
def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request, 'listings/band_detail.html', { 'band': band })

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)

    else:
        form = BandForm()

    return render(request,
            'listings/band_create.html',
            {'form': form})

def band_update(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)
    return render(request, 'listings/band_update.html', {'form': form})

def band_delete(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        band.delete()
        return redirect('band-list')

    return render(request, 'listings/band_delete.html', { 'band': band })

def about(request):
    return HttpResponse('<h1>A Propos</h1> <p>Nous adorons merch !</p>')

def listings(request):
    titles = Title.objects.all()
    return render(request, 'listings/listings.html', {'titles': titles})

def listing_detail(request, id):
    title = Title.objects.get(id=id)
    return render(request, 'listings/listing_detail.html', { 'title': title })

def listing_create(request):
    if request.method == 'POST':
        form = TitleForm(request.POST)
        if form.is_valid():
            title = form.save()
            return redirect('listing-detail', title.id)

    else:
        form = TitleForm()

    return render(request,
            'listings/listing_create.html',
            {'form': form})

def listing_update(request, id):
    title = Title.objects.get(id=id)
    if request.method == 'POST':
        form = TitleForm(request.POST, instance=title)
        if form.is_valid():
            title = form.save()
            return redirect('listing-detail', title.id)
    else:
        form = TitleForm(instance=title)
    return render(request, 'listings/listing_update.html', {'form': form})

def listing_delete(request, id):
    title = Title.objects.get(id=id)

    if request.method == 'POST':
        title.delete()
        return redirect('listing-list')

    return render(request, 'listings/listing_delete.html', { 'title': title })

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