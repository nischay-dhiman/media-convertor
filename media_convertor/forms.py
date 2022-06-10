from django import forms


class DocumentForm(forms.Form):
    mediafile = forms.FileField(label='Select a file', required=False)
    mediaUrl = forms.CharField(label='Paste Wav file Url', max_length=1000, required=False, widget=forms.TextInput(attrs={'placeholder': 'Paste .wav url'}))


def has_media_file():
    return False

def has_media_url():
    return True
