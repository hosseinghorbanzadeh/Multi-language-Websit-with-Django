from django import forms

#from django.forms import ModelForm
from blog.models import Contact,Newsletter
from captcha.fields import CaptchaField


class NameForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    email = forms.EmailField(label='email')
    subject = forms.CharField(label='subject',max_length=100)
    message = forms.CharField(widget=forms.Textarea)



class Contactform(forms.ModelForm):
    #subject = forms.CharField(required=False)
    captcha = CaptchaField()
    class Meta:
        model=Contact
        fields ='__all__'


class Newsletterform(forms.ModelForm):
    class Meta:
        model=Newsletter
        fields ='__all__'