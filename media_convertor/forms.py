from django import forms


class DocumentForm(forms.Form):
    mediafile = forms.FileField(label='Select a file')