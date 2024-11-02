from dataclasses import fields
from tkinter import Widget
from django import forms
from rsa import encrypt
from .models import Models
'''
class Modelsform(forms.ModelForm):
    class Meta:
        model = Models
        fields = [
            'model_name',
            'disease',
            'model_file',
            'description',
            'preprocessing',
            'engID',
            'meta_data'
        ]
        enctype = "multipart/form-data"
        widgets = {
            'model_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'model_file' : forms.ClearableFileInput(attrs={'class' : 'form-control', 'enctype': enctype ,'multiple': True}),
            'description' : forms.Textarea(attrs={'class' : 'form-control'}),
            'preprocessing' : forms.Textarea(attrs={'class' : 'form-control'}),
            'disease' : forms.Select(attrs={'class' : 'form-control'}),
            'engID' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'meta_data' : forms.Textarea(attrs={'class' : 'form-control'}),
        }
'''