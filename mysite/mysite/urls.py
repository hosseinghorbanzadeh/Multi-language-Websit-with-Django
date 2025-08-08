"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from blog.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import StaticViewSitemap
from blogpage.sitemaps import BlogSitemap

from debug_toolbar.toolbar import debug_toolbar_urls
import debug_toolbar

from blog.views import *

#app_name = 'mysite'

sitemaps = {
    'static': StaticViewSitemap,
    'blogpage':BlogSitemap
}

urlpatterns = [
    #re_path(r'^.*$', coming_soon),
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),  
    path('blog/', include('blogpage.urls', namespace='blogpage')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', include('robots.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('summernote/', include('django_summernote.urls')),
    path('captcha/', include('captcha.urls')),
    #path('accounts/',include('django.contrib.auth.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
