from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import *

class time_range(ModelForm):
    class Meta:
        model = Timing
        fields = ('start_time', 'end_time')

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if Timing.objects.filter(start_time__lte0 = end_time, end_time__gte = start_time).exists():
            raise ValidationError("Time range specified with pre-existing time range")