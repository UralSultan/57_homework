from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User


# class MyUserCreateForm(forms.ModelForm):
#     password = forms.CharField(label='Пароль', strip=False, required=True, widget=forms.PasswordInput)
#     password_confirm = forms.CharField(label='Подтверждение пароля', strip=False, required=True, widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password', 'password_confirm', 'first_name', 'last_name')
#
#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get('password')
#         password_confirm = cleaned_data.get('password_confirm')
#
#         if password and password_confirm and password != password_confirm:
#             self.add_error('password_confirm', 'Пароли не совпадают.')
#
#         return cleaned_data
#
#     def clean_password(self):
#         password = self.cleaned_data.get('password')
#         if password:
#             validate_password(password, user=self.instance)
#         return password
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data['password'])
#
#         if commit:
#             user.save()
#             self.save_m2m()
#
#         return user
#

class MyUserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name',)



