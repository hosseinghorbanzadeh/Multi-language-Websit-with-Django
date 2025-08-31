from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from blog.models import *
from blog.forms import Newsletterform,Contactform
from django.contrib import messages
from blogpage.models import Post,Comment
from django.http import HttpResponse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.utils import timezone
from taggit.models import Tag

# Create your views here.

def home(request,**kwargs):
    all_tags = Tag.objects.all()
    now=timezone.now()
    posts=Post.objects.filter(published_date__lte=now,status=True)
    
    if kwargs.get('cat_name') != None:
        posts=posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts=posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
    
    posts=Paginator(posts,3)

    try:
        page_number = request.GET.get("page")
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts=posts.get_page(1)
    except EmptyPage:
        posts=posts.get_page(1)
    
    context={"posts":posts,
              "all_tags": all_tags,
              'section': 'home',
             }

    return render(request, 'website\index.html', context)




def about(request):
    context = {
        'section': 'about',  # نمایش بخش درباره ما
    }
    return render(request, 'website\index.html', context)


def blog(request):
    context = {
        'section': 'blog',  # نمایش بخش درباره ما
    }
    return render(request, 'website\index.html', context)

def services(request):
    context = {
        'section': 'services',  # نمایش بخش درباره ما
    }
    return render(request, 'website\index.html', context)


def portfolio(request):
    context = {
        'section': 'portfolio',  # نمایش بخش درباره ما
    }
    return render(request, 'website\index.html', context)

def contact(request):
    context = {
        'section': 'contact',  # نمایش بخش درباره ما
    }
    return render(request, 'website\index.html', context)