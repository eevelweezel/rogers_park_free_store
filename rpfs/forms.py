from captcha.fields import CaptchaField
from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from .models import Category


class CaptchaContactForm(forms.Form):

    captcha = CaptchaField()

    def send_email(self):
        send_mail(self.subject,
                  self.cleaned_data, 
                  self.cleaned_data['email'],
                  [settings.MAIL_RECIPIENT],
                  fail_silently=False)

#below needing to be reformatted? Check
#class ContactForm(ModelForm):
#    class Meta:
#        model = Contact
#        fields = '__all__'

class ContactForm(CaptchaContactForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.subject = 'Contact inquiry'

    name = forms.CharField(label=_('Your name'), required=True)
    email = forms.EmailField(label=_('Email'), required=True)
    subject = forms.CharField(label=_('Subject'), required=True)
    message = forms.CharField(label=_('Message'), widget=forms.Textarea, required=True) 
    #category = forms.ChoiceField(choices[('general information', 'General Information'), ('donation', 'Donation'), ('pickup', 'Pickup'), ('other', 'Other')])
    #if I wasn't using a Django widgit, would I need to specift a char_limit for "message"? 

class VolunteerForm(CaptchaContactForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.subject =_('Volunteer inquiry')

    name = forms.CharField(label=_('Your name'), required=True) 
    email = forms.EmailField(label=_('Email'), required=True)
    pronouns = forms.CharField(label=_('Pronouns'), required=True)
    message = forms.CharField(label=_('Message'), widget=forms.Textarea, required=True)
    VOLUNTEER_CHOICES = (
            ('a', _('Working at the Free Store location during "closed to public" times (organizing the space, putting supply packages together, etc.)')),
            ('b', _('Working at the Free Store location during "open to public" times (handing out requested supplies, helping neighbors make supply requests, etc.)')),
            ('c', _('Delivering supplies either from or to the Free Space (will need a car)')),
            ('d', _('Volunteer Coordination/Training/Support (can be working from home)')),
            ('e', _('Inventory and/or financial book-keeping (can be working from home)')),
            ('f', _('Outreach and/or social media (can be working from home)')),
            ('g', _('Translation (Spanish, French, Chinese, others if applicable)')),
            ('h', _('Other')),
    )
    volunteer_field = forms.MultipleChoiceField(label=_('Volunteer Positions'), widget=forms.CheckboxSelectMultiple, choices = VOLUNTEER_CHOICES)

    