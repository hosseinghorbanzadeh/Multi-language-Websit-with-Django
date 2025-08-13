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
'''
def index_view(request, **kwargs):
    all_tags = Tag.objects.all()
    now = timezone.now()
    posts = Post.objects.filter(published_date__lte=now, status=True)
    
    if kwargs.get('cat_name') is not None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') is not None:
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') is not None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
    
    context = {
        "posts": posts,
        "all_tags": all_tags,
    }
    print('========================',posts.count())
    return render(request,'website/index.html',context)
'''

def index_view(request,**kwargs):
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
             }
    return render(request,'website/index.html',context)


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
    return render(request,'website/blog-post-1.html',{"form": form})






