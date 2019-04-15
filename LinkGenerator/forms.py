from django import forms
from LinkGenerator.models import RedirectorModel

EMPTY_ORIGINAL_LINK_ERROR = "You can't have an empty list item"

# class LinkGeneratorForm(forms.Form):
#     original_link = forms.URLField(widget=forms.fields.TextInput(attrs={
#         'placeholder': 'Insert a link you want to shorten',
#         'class': 'form-control input-lg'
#     }))


class LinkGeneratorForm(forms.models.ModelForm):

    class Meta:
        model = RedirectorModel
        fields = ('original_link',)
        widgets = {
            'original_link' : forms.fields.TextInput(attrs={
                'placeholder': 'Insert a link you want to shorten.',
                'class': 'form-control input-lg',
            })
        }

        error_messages = {
            'text': {'required': EMPTY_ORIGINAL_LINK_ERROR}
        }