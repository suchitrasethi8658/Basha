from socket import fromshare
from django import forms
from app.models import *
class SuchiForm(forms.ModelForm):
    class Meta:
        model=Suchi
        fields='__all__'

class BashaForm(forms.ModelForm):
    class Meta:
        model=Basha
        fields='__all__'
        