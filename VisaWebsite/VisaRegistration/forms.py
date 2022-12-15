from django import forms
from django.contrib.auth import get_user_model
from VisaWebsite import settings
from .models import Visa, User


class VisaForm(forms.ModelForm):
    class Meta:
        model = Visa
        fields = ['first_name', 'surname', 'series_passport',
                  'country', 'visa_type', 'tariff_number', 'phone', 'email']
        widgets = {
            'phone': forms.TextInput(attrs={
                'class': 'form-control phone',
                'placeholder':'+380 (__) ___ __ __'}
                                     )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = "Ім'я"
        self.fields['surname'].label = 'Прізвище'
        self.fields['series_passport'].label = "Серія закордоного паспорту та номер"
        self.fields['country'].label = "Країна"
        self.fields['visa_type'].label = 'Тип візи'
        self.fields['tariff_number'].label = 'Срок дії візи'
        self.fields['phone'].label = 'Номер телефону'
        self.fields['email'].label = 'Електронна пошта'


class LoginForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Ім'я користувача"
        self.fields['username'].help_text = None
        self.fields['password'].label = 'Пароль'

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = User.objects.filter(username=username).first()
        if not user:
            raise forms.ValidationError(f'Дані авторизації введені невірно')
        if not user.check_password(password):
            raise forms.ValidationError(f'Дані авторизації введені невірно')
        return self.cleaned_data


class DateInput(forms.DateInput):
    input_type = 'date'


class RegistrationForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    birthday = forms.DateField(widget=DateInput, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Ім'я користувача"
        self.fields['username'].help_text = "Вимагається 150 символів або менше. Лише літери, цифри та @/./+/-/_."
        self.fields['password'].label = 'Пароль'
        self.fields['confirm_password'].label = 'Підтвердьте пароль'
        self.fields['first_name'].label = "Ім'я"
        self.fields['last_name'].label = "Прізвище"
        self.fields['email'].label = 'Електронна пошта'
        self.fields['birthday'].label = 'Дата народження'

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Цей імейл вже зареєстрований')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Це ім'я користувача вже зареєстроване")
        return username

    def clen(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise  forms.ValidationError('Невідповідність пароля')
        return self.cleaned_data

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'birthday', 'password', 'confirm_password']
        widgets = {
            'birthday': forms.DateInput(
                format=('%D-%M-%Y'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       })
        }


class ButtonForm(forms.Form):
    btn = forms.CharField()