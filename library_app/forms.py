from django import forms
from django.forms.models import ModelForm
from .models import Books

class addBook(ModelForm):
    class Meta:
        model = Books
        fields = "__all__"
