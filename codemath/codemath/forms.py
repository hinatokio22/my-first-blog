from  django import forms
from  .models import convertir

class convertform(forms.ModelForm):

    class meta:
        model=convertir

        fields=[
            'numeroDecimal',
            'numeroBinario',
            'numeroOctal',
            'numeroHexadecimal',
        ]
        labels={
            'numeroDecimal': 'numeroDec a convertir',
            'numeroBinario': 'numeroBin a convertir',
            'numeroOctal': 'numeroOct a convertir',
            'numeroHexadecimal': 'numeroHex a convertir',
        }
        widgets={
            'numeroDecimal': forms.TextInput(attrs={'class': 'form-control'}),
            'numeroBinario': forms.TextInput(attrs={'class': 'form-control'}),
            'numeroOctal': forms.TextInput(attrs={'class': 'form-control'}),
            'numeroHexadecimal': forms.TextInput(attrs={'class': 'form-control'}),
        }
