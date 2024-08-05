from django import forms


class ItemForm(forms.Form):
    file = forms.FileField()
