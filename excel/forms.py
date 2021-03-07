from django import forms
from .models import file


class file_form(forms.ModelForm):
    class Meta:
        model= file
        fields= ['file_field']