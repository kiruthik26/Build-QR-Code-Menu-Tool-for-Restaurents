from django import forms

class QRCodeForm(forms.Form):
    restaurent_name = forms.CharField(
        label='Restaurant Name',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the name of the restaurant'
        })
    )
    
    url = forms.URLField(
        label='Menu URL',
        max_length=200,
        widget=forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the menu URL'
        })
    )
