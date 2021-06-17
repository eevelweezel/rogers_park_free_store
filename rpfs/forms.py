from captcha.fields import CaptchaField
from django import forms
from django.conf import settings
from django.core.mail import send_mail
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

    def __init__(self):
        super().__init__(*args, **kwargs)
        self.subject = 'Contact inquiry'

    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True) 
    #category = forms.ChoiceField(choices[('general information', 'General Information'), ('donation', 'Donation'), ('pickup', 'Pickup'), ('other', 'Other')])
     
class VolunteerForm(CaptchaContactForm):

    def __init__(self):
        super().__init__(*args, **kwargs)
        self.subject = 'Volunteer inquiry'

    name = forms.CharField(required=True) 
    email = forms.EmailField(required=True)
    #phone = forms.RegexField(regex='*') 
    pronouns = forms.CharField(required=True)
    #DROP BOX "how did you hear about us" *use dropbox from above
    message = forms.CharField(widget=forms.Textarea, required=True)
    VOLUNTEER_CHOICES = (
            ('Working at the Free Store location during "closed to public" times (organizing the space, putting supply packages together, etc.)'),
            ('Working at the Free Store location during "open to public" times (handing out requested supplies, helping neighbors make supply requests, etc.)'),
            ('Delivering supplies either from or to the Free Space (will need a car)'),
            ('Volunteer Coordination/Training/Support (can be working from home)'),
            ('Inventory and/or financial book-keeping (can be working from home)'),
            ('Outreach and/or social media (can be working from home)'),
            ('Translation (Spanish, French, Chinese, others if applicable)'),
            ('Other'),
     
        )
    title = forms.MultipleChoiceField(choices =VOLUNTEER_CHOICES)