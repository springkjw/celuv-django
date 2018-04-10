from django import forms
from django_select2 import forms as select2_forms

from .models import Celebrity
from apps.entertainments.models import Entertainment


class CelebrityForm(forms.ModelForm):
    entertainment = forms.ModelMultipleChoiceField(
        label="소속 기획사",
        queryset=Entertainment.objects.all(),
        widget=select2_forms.Select2MultipleWidget,
        required=False,
    )

    class Meta:
        model = Celebrity
        fields = [
            'image',
            'entertainment',
            'name',
            'celeb_type',
            'real_name',
            'debut',
            'birth',
            'sex',
        ]
