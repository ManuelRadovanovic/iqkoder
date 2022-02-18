from django import forms
from django.forms import ModelForm

from .models import Continents, Countries

# Create a continent form
class ContinentForm(ModelForm):
    class Meta:
        model = Continents
        fields = "__all__"

        labels = {
            'continent_de' : '',
            'continent_en' : '',
            'continent_sr' : '',
            
        }

        widgets = {
            'continent_de' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kontinent DE'}),
            'continent_en' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kontinent EN'}),
            'continent_sr' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kontinent SR'}),
        }


# Create a country form
class CountryForm(ModelForm):
    class Meta:
        model = Countries
        fields = "__all__"

        labels = {
            'country_de' : '',
            'country_en' : '',
            'country_sr' : '',
            'continent' : 'Kontinent',
            'flag' : 'Zastava'
            
        }

        widgets = {
            'country_de' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zemlja DE'}),
            'country_en' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zemlja EN'}),
            'country_sr' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zemlja SR'}),
        }




