from django import forms


class LinkGeneratorForm(forms.Form):
    original_link = forms.URLField()