from django import forms
from django.forms import ModelForm
from .models import producto

class ProductoForm(ModelForm):
    class Meta:
        model = producto
        fields = "__all__"
        widgest = {
            'nombreproducto':forms.TextInput(
                attrs={
                    'placeholder':'Debe ingresar el nommbre',
                    'class':'form-control'
                }
            ),
            'precio':forms.TextInput(
                attrs={
                    'placeholder':'Debe ingresar un valor',
                    'class':'form-control'
                }
            ),
            'categoria':forms.Select(
                attrs={
                    'class':'form-control'
                }
            )
        }