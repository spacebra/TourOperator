from django import forms

from django.core.files.uploadedfile import SimpleUploadedFile

from program.models import Program, Picture

class CreateForm(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(max_length=10000)
    price = forms.DecimalField(max_digits=9, decimal_places=2)
    picture = forms.ImageField()

