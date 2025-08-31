from django.urls import path
from blog.views import *
from django.urls import include, path



app_name = 'blog'   
urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    #path('blog/', blog, name='blog'),
    path('services/', services, name='services'),
    path('portfolio/', portfolio, name='portfolio'),
    path('contact/', contact, name='contact'),
]