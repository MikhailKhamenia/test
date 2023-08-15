from django import forms
from .models import Reader

class ReaderForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = ['last_name', 'first_name', 'patronymic']

