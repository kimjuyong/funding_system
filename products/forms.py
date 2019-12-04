from django import forms
from django_countries.fields import CountryField
from . import models


class SearchForm(forms.Form):

    car_model = forms.CharField(initial="Anything")
    manufactureCountry = CountryField(default="KR").formfield()
    car_type = forms.ModelChoiceField(
        required=False, empty_label="Any kind", queryset=models.CarType.objects.all()
    )
    guests = forms.IntegerField(required=False)
    seats = forms.IntegerField(required=False)
    efficiency = forms.IntegerField(required=False)
    instant_book = forms.BooleanField(required=False)
    facility = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Facility.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
