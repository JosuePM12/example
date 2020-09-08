from django import forms
from .models import Bodega

class bodegaForm(forms.ModelForm):
    class Meta:
        model=Bodega
        fields=['nombre','descripcion','cantidad']