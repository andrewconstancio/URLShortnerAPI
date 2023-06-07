from django import forms

class URL(forms.Form):
    url = forms.CharField(label="URL")