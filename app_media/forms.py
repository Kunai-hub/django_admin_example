from django import forms

from app_media.models import File


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=100)
    file = forms.FileField()


class DocumentForm(forms.ModelForm):

    class Meta:
        model = File
        fields = ('description', 'file')
