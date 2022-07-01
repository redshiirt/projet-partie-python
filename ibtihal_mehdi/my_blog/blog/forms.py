from django.forms import ModelForm
from django import forms
from .models import  commande, produit
class productForm(ModelForm):
    class Meta:
        model =produit
       
        fields ='__all__'

class commandForm(ModelForm):
    class Meta:
        model =commande
       
        fields ='__all__'