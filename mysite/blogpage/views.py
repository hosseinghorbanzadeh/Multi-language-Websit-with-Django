
from django.shortcuts import render,get_object_or_404,HttpResponse,redirect
from blogpage.models import Post,Comment,Category
from django.utils import timezone
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from taggit.models import Tag
from blogpage.froms import Commentform
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from blog.forms import Newsletterform,Contactform
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.



def blog_view(request, **kwargs):
    # گرفتن همه تگ‌ها
    all_tags = Tag.objects.all()
    all_categories = Category.objects.all()  # گرفتن همه دسته‌بندی‌ها

    # فیلتر کردن پست‌ها بر اساس تاریخ و وضعیت
    now = timezone.now()
    posts = Post.objects.filter(published_date__lte=now, status=True)

    # فیلتر کردن بر اساس دسته‌بندی (در صورتی که مقدار `cat_name` ارسال شده باشد)
    if kwargs.get('cat_name') is not None:
        posts = posts.filter(category__name=kwargs['cat_name'])

    # فیلتر کردن بر اساس نام کاربر (در صورتی که `author_username` ارسال شده باشد)
    if kwargs.get('author_username') is not None:
        posts = posts.filter(author__username=kwargs['author_username'])

    # فیلتر کردن بر اساس تگ (در صورتی که `tag_name` ارسال شده باشد)
    if kwargs.get('tag_name') is not None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
        
    posts=Paginator(posts,4)
    try:
        page_number = request.GET.get("page")
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts=posts.get_page(1)
    except EmptyPage:
        posts=posts.get_page(1)
    

    # ایجاد context برای ارسال به قالب
    context = {
        'posts': posts,
        'all_tags': all_tags,  # ارسال همه تگ‌ها
        'all_categories': all_categories,  # ارسال همه دسته‌بندی‌ها
        'section': 'blog',  # بخش بلاگ
    }

    return render(request, 'website/index.html', context)



def blog_single(request,pid):
    if request.method=='POST':
        #print('============request.method================')
        form = Commentform(request.POST)
        if form.is_valid():
            form.save()
            #print('============save================')
            messages.add_message(request, messages.SUCCESS, "Comment saved successfully.after approve with admin you can see it")
        else:
            messages.add_message(request, messages.ERROR, "Comment don't saved !")
   
    now = timezone.now()
    post=get_object_or_404(Post,pk=pid,published_date__lte=now,status=True)
    next_post = Post.objects.filter(id__gt=post.id,published_date__lte=now,status=True).order_by('id').first()
    prev_post = Post.objects.filter(id__lt=post.id,published_date__lte=now,status=True).order_by('-id').first()
    #print('============show================',request.method)
    if not post.login_require:
        comments=Comment.objects.filter(post=post.id,approve=True)
        comments_count = comments.count()
        form=Commentform()
        post.counted_views += 1
        post.save()
        return render(request, 'website/blog-single.html', {
                'post': post,
                'next_post': next_post,
                'prev_post': prev_post,
                'comments':comments,
                'comments_count': comments_count,
                'form':form,
        })
    else:
        if  request.user.is_authenticated:
            comments=Comment.objects.filter(post=post.id,approve=True)
            comments_count = comments.count()
            form=Commentform()
            post.counted_views += 1
            post.save()
            return render(request, 'website/blog-single.html', {
                            'post': post,
                            'next_post': next_post,
                            'prev_post': prev_post,
                            'comments':comments,
                            'comments_count': comments_count,
                            'form':form,
                    })
        return HttpResponseRedirect(reverse('login'))
        
        #return redirect('/')


def blog_search(request):
    now=timezone.now()
    posts=Post.objects.filter(published_date__lte=now,status=True)
    if request.method == "GET":
        if s:=request.GET.get('s'):
            posts=posts.filter(content__contains=s)
        #posts=posts.filter(content__contains=request.GET.get('s'))
    
    context={"posts":posts}
    return render(request,'blog/blog-home.html',context)




