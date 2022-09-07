
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

from listings.models import Band
from listings.models import Title
from listings.forms import ContactUsForm


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})
    
def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request, 'listings/band_detail.html', { 'band': band })

def about(request):
    return HttpResponse('<h1>A Propos</h1> <p>Nous adorons merch !</p>')

def listings(request):
    titles = Title.objects.all()
    return render(request, 'listings/listings.html', {'titles': titles})

def listing_detail(request, id):
    title = Title.objects.get(id=id)
    return render(request, 'listings/listing_detail.html', { 'title': title })

def contact(request):

    print('Les méthodes de requête est :', request.method)
    
    if request.method == 'POST':

        form = ContactUsForm(request.POST)



        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via Merchex Contact Us form',
                from_email=form.cleaned_data['email'],
                recipient_list=['EMAIL_BACKENd'],
            )

    else:
        form = ContactUsForm()

    return render(request, 
            'listings/contact.html', 
            {'form': form})