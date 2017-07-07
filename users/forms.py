from django import forms
from django.contrib.auth.models import User
from django.forms.utils import ErrorList


class UserForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    name_company = forms.CharField(required=True)

    def is_valid(self):
        valid = True
        if not super(UserForm, self).is_valid():
            self.add_erro('Por favor, verifique os dados informados')
            valid = False
        user_exists = User.objects.filter(username=self.data['name']).exists()
        if user_exists:
            self.add_erro('Usuario ja existente')
            valid = False

        return valid

    def add_erro(self, message):
        self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, ErrorList()).append(message)
