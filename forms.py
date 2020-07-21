from django import forms


class MyForm(forms.Form):
    weight=forms.CharField(label="weight",max_length=20)
    height=forms.CharField(label="height",max_length=20)