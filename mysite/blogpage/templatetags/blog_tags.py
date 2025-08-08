
from django import template
from blogpage.models import Post,Category,Comment
from django.utils import timezone


register = template.Library()

#@register.simple_tag(takes_context=True)
@register.simple_tag(name="post")
def function():
    now = timezone.now()
    return Post.objects.filter(published_date__lte=now,status=True)[:3]



@register.simple_tag(name="comments_count")
def function(pid):
    return Comment.objects.filter(post=pid,approve=True).count()


@register.filter
def snippet(value,arg=10):
    return value[0:arg] + '...'

@register.inclusion_tag('blog/popularposts.html')
def popularposts(arg=3):
    now = timezone.now()
    posts=Post.objects.filter(published_date__lte=now,status=True).order_by('-published_date')[:arg]
    return {"posts":posts}


@register.inclusion_tag('blog/categorypost.html')
def categorypost(arg=3):
    now = timezone.now()
    posts=Post.objects.filter(published_date__lte=now,status=True)
    category=Category.objects.all()
    cat_dict={}
    for name in category:
        #cat_dict.update({name:Post.objects.filter(category=name).count()})
        cat_dict[name]=posts.filter(category=name).count()
    return {"categorys":cat_dict}


@register.inclusion_tag('blog/last_post_index.html')
def lastpost(arg=6):
    now = timezone.now()
    posts=Post.objects.filter(published_date__lte=now,status=True).order_by('-published_date')[:arg]
    return {"posts":posts}


