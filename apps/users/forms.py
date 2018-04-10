from django import forms

from .models import MyUser


class UserFanForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = [
            'username',
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
            'username',
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
