from django.urls import path
from blog.views import *
from django.urls import include, path


app_name = 'blog'  
urlpatterns = [
    path('', index_view, name='index'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
    path('elements/', elements_view, name='elements'),
    path('newsletters/', newsletters_view, name='newsletters'),
    
    path('test/', test, name='test'),
]