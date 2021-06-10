from captcha.fields import CaptchaField
from django import forms
from django.conf import settings
from django.core.mail import send_mail


class CaptchaContactForm(forms.Form):
    # TODO: the fields listed here and references to self.cleaned_data 
    # in send_email() need to point to fields on the Volunteer Signup Form.
    # BUT! captcha field should stay as-is...

    # For each field, you'll want to add the text from the google form as
    # a field attribute. You can use this as a template for other forms.
    email = forms.CharField()
    subject = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    captcha = CaptchaField()

    def send_email(self):
        send_mail(self.cleaned_data['subject'],
                  self.cleaned_data['content'],
                  self.cleaned_data['email'],
                  [settings.MAIL_RECIPIENT],
                  fail_silently=False)
