from django import forms
from django.forms import ModelForm
from .models import Pizza, Ingredient, Size


class PizzaForm(ModelForm):
    class Meta:
        model = Pizza
        fields = ['name', 'price', 'size', 'description','available','ingredient']
