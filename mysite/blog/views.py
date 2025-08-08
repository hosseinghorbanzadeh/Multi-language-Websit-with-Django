from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from blog.models import *
from blog.forms import Newsletterform,Contactform
from django.contrib import messages

from django.http import HttpResponse


# Create your views here.

def index_view(request):
    return render(request,'website/index.html')


def about_view(request):
    return render(request,'about.html')

def contact_view(request):
    if request.method == 'POST':
        form = Contactform(request.POST)
        if form.is_valid():
            form.instance.name="Unknown"
            form.save()
            messages.add_message(request, messages.SUCCESS, "Form saved successfully.")
        else:
            messages.error(request, 'The form was not saved successfully.!')

    form = Contactform()
    return render(request,'contact.html',{"form": form})

#======================================================================

def elements_view(request):
    return render(request,'elements.html')


def newsletters_view(request):
    if request.method == 'POST':
        form= Newsletterform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


def test(request):
    tmp_dict={}
    if request.method == 'POST':
        form = Contactform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Form saved successfully. !')
        else:
            return HttpResponse('The form was not saved successfully.!')

    form = Contactform()
    return render(request,'test.html',{"form": form})






