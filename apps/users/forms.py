from django import forms
from django.forms import inlineformset_factory
from django_select2 import forms as select2_forms

from .models import MyUser
from apps.celebritys.models import Celebrity
from apps.entertainments.models import Manager


class UserFanForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = [
            'email',
            'phone'
        ]


class UserManagerForm(forms.ModelForm):
    password = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput({
            'placeholder': '비밀번호'
        })
    )
    password1 = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput({
            'placeholder': '비밀번호 확인'
        })
    )

    class Meta:
        model = MyUser
        fields = [
            'email',
            'password',
            'password1',
            'name',
            'phone',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                if type(field.widget) in (forms.TextInput, forms.EmailInput):
                    field.widget = forms.TextInput(
                        attrs={'placeholder': field.label})

    def clean(self):
        if self.cleaned_data['password'] != self.cleaned_data['password1']:
            raise forms.ValidationError('비밀번호을 다시 확인해주세요.')

    def save(self, commit=True):
        user = super().save(commit)
        user.is_manager = True
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class ManagerForm(forms.ModelForm):
    celebrity = forms.ModelMultipleChoiceField(
        label="담당 셀럽",
        queryset=Celebrity.objects.all(),
        widget=select2_forms.Select2MultipleWidget,
        required=False,
    )

    class Meta:
        model = Manager
        fields = [
            'entertainment',
            'manager_type',
            'position',
            'celebrity',
        ]


ManagerFormSet = inlineformset_factory(
    MyUser, Manager, form=ManagerForm, extra=1, can_delete=False)
