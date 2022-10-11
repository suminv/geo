from django import forms
from measurements.models import Measurement


class MeasurementModelForm(forms.ModelForm):
    destination = forms.CharField()


    class Meta:
        model = Measurement
        fields = ('destination',)


