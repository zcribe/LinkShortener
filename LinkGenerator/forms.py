from django import forms


class LinkGeneratorForm(forms.Form):
    original_link = forms.URLField(widget=forms.fields.TextInput(attrs={
        'placeholder': 'Insert a link you want to shorten',
        'class': 'form-control input-lg'
    }))