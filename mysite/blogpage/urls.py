from django.urls import path
from blogpage.views import *
#from django.conf import settings
#from django.conf.urls.static import static
from blogpage.feeds import LatestEntriesFeed

app_name = 'blogpage'  

urlpatterns = [
    path('', blog_view, name='blog'),
    path('<int:pid>' ,blog_single,name='single'),
    path('author/<str:author_username>' ,blog_view,name='author'),
    path('category/<str:cat_name>' ,blog_view,name='category'),
    path('tag/<str:tag_name>' ,blog_view,name='tag'),
    #path('search/',blog_search,name='search'),
    path('rss/feed/', LatestEntriesFeed()),
] 