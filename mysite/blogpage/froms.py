from django import forms

#from django.forms import ModelForm
from blogpage.models import Comment
from captcha.fields import CaptchaField

'''
class CommentForm(forms.Form):
    #post
    
    #email
    #subject
    #message
    name = forms.CharField(label='name', max_length=100)
    email = forms.EmailField(label='email')
    subject = forms.CharField(label='subject',max_length=100)
    message = forms.CharField(widget=forms.Textarea)

'''

class Commentform(forms.ModelForm):
    #captcha = CaptchaField()
    class Meta:
        model=Comment
        fields =['post','name','email','subject','message']

