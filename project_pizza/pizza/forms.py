from django import forms
from .models import Pizza, Ingredient, Size


class PizzaForm(forms.Form):
    name = forms.CharField(max_length=40)
    price = forms.DecimalField()
    size = forms.ModelChoiceField(queryset=Size.objects.all())
    description = forms.CharField(max_length=300)
    available = forms.BooleanField()
    ingredient = forms.ModelMultipleChoiceField(queryset=Ingredient.objects.all())

    def create_objects(self):
        Pizza.objects.create(
            name=self.cleaned_data.get('name'),
            price=self.cleaned_data.get('price'),
            size = self.cleaned_data.get('size'),
            description=self.cleaned_data.get('description'),
            available=self.cleaned_data.get('available'),
        )
