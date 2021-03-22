from django import forms
from django.forms import Textarea

from .validators import *


class ValidForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(validators=[validate_domainonly_email])
    # email2 = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea())

    # def clean_email(self):
    # '''
    # field level validation --- show field errors
    # '''
    # email_passed = self.cleaned_data.get('email')
    # email2_passed = self.cleaned_data.get('email2')
    # email_req = 'lalala@gmail.com'
    # if not email_req in email_passed:
    #     raise forms.ValidationError('Not a valid email')
    # if email2_passed != email_passed:
    #     raise forms.ValidationError('Second email must be like first')
    # return email_passed
    #
    # def clean(self):
    #     '''
    #     form level validation --- non-field errors . show whole form error
    #     '''
    #     cleaned_data = super(ValidForm, self).clean()
    #     email_passed = cleaned_data.get('email')
    #     email_req = 'lalala@gmail.com'
    #     if not email_req in email_passed:
    #         raise forms.ValidationError('Not a valid email')
