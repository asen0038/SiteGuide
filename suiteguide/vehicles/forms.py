from django import forms
from .models import Vehicle


class VehicleForm(forms.ModelForm):

    class Meta:

        model = Vehicle

        #Vehicle fields
        fields = [
            "vehicle_type",
            "company",
            "model",
            "color",
            "passenger_capacity",
            "mass_kg",
        ]
