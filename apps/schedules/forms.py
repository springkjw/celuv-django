from django import forms
from django_select2 import forms as select2_forms

from .models import Schedule
from apps.celebritys.models import Celebrity


class ScheduleForm(forms.ModelForm):
    # 스케줄 폼
    celebrity = forms.ModelMultipleChoiceField(
        label="담당 셀럽",
        queryset=Celebrity.objects.all(),
        widget=select2_forms.Select2MultipleWidget,
        required=False,
    )

    class Meta:
        model = Schedule
        fields = (
            'schedule',
            'title',
            'celebrity',
            'url',
        )
