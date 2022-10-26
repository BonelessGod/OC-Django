from django import forms
from listings.models import Band, Title

class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea, max_length=1000)

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        exclude = ('active', 'official_website')

class TitleForm(forms.ModelForm):
    class Meta:
        model = Title
        exclude = ('sold',)