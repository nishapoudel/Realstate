from dataclasses import fields
from django import forms

from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields=['name','location','area','category','filter_price','price','image','created_date']
        widgets = {
             'name': forms.TextInput(attrs={'class': 'form-control'}),
              'location': forms.TextInput(attrs={'class': 'form-control'}),
               'area': forms.TextInput(attrs={'class': 'form-control'}),


            'category': forms.Select(attrs={'class': 'form-control'}),
            'filter_price': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),

            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name' : ' Name:',
             'location' : ' Location:',
              'area' : ' Area:',

            'category': 'Select Category: ',
             'filter_price': 'Select an price range: ',
            'price': 'Enter a price: ',
             'image': 'Select an Image: ',

        }
