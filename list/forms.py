from django import forms
from .models import list
class post(forms.ModelForm):
    class Meta:
        model=list
        fields='__all__'
        exclude=('done',)