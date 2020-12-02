from django.forms import ModelForm
from .models import Car, Person


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
