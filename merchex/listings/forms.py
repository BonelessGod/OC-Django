from django import forms
from listings.models import Band

class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea, max_length=1000)

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = '__all__'