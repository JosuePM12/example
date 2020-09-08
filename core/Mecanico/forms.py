from django import forms
from .models import Mecanico

class MecanicoForm(forms.ModelForm):
    class Meta:
        model=Mecanico
        fields=['apellido','nombre','edad','email','cedula','sexo']