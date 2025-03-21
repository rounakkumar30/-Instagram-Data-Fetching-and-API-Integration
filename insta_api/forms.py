from django import forms

class InstagramForm(forms.Form):
    username = forms.CharField(label="Instagram Username", max_length=50)
