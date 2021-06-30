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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.subject = 'Contact inquiry'

    name = forms.CharField(label='Your name', required=True)
    email = forms.EmailField(label='Email', required=True)
    subject = forms.CharField(label='Subject', required=True)
    message = forms.CharField(label='Message', widget=forms.Textarea, required=True) 
    #category = forms.ChoiceField(choices[('general information', 'General Information'), ('donation', 'Donation'), ('pickup', 'Pickup'), ('other', 'Other')])
    #if I wasn't using a Django widgit, would I need to specift a char_limit for "message"? 

class VolunteerForm(CaptchaContactForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.subject = 'Volunteer inquiry'

    name = forms.CharField(label='Your name', required=True) 
    email = forms.EmailField(label='Email', required=True)
    pronouns = forms.CharField(label='Pronouns', required=True)
    message = forms.CharField(label='Message', widget=forms.Textarea, required=True)
    VOLUNTEER_CHOICES = (
            ('a', 'Working at the Free Store location during "closed to public" times (organizing the space, putting supply packages together, etc.)'),
            ('b', 'Working at the Free Store location during "open to public" times (handing out requested supplies, helping neighbors make supply requests, etc.)'),
            ('c', 'Delivering supplies either from or to the Free Space (will need a car)'),
            ('d', 'Volunteer Coordination/Training/Support (can be working from home)'),
            ('e', 'Inventory and/or financial book-keeping (can be working from home)'),
            ('f', 'Outreach and/or social media (can be working from home)'),
            ('g', 'Translation (Spanish, French, Chinese, others if applicable)'),
            ('h', 'Other'),
    )
    volunteer_field = forms.MultipleChoiceField(label='Volunteer Positions', choices = VOLUNTEER_CHOICES)

    
    #how render this form into a view??? Do we need to create code in views.py?

#    title = forms.MultipleChoiceField(choices =VOLUNTEER_CHOICES)