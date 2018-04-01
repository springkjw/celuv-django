from django import forms

from .models import Entertainment


class EntertainmentForm(forms.ModelForm):
    class Meta:
        model = Entertainment
        fields = (
            'name',
            'image',
            'start',
            'homepage',
            'code',
        )
