# coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin

#from article import views as articleviews
#from article.templatetags import custom_markdown 
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', articleviews.home),
    url(r'^$', 'article.views.home', name = 'home'),
    #url(r'^(?P<my_args>\d+)/$', articleviews.detail, name='detail'),
    #url(r'^test/$', articleviews.test),
    url(r'^(?P<id>\d+)/$', 'article.views.detail', name='detail'),
    url(r'^archives/$', 'article.views.archives', name = 'archives'),
    url(r'^aboutme/$', 'article.views.about_me', name = 'about_me'),
    #url(r'^tag(?P<tag>\w+)/$', 'article.views.search_tag', name = 'search_tag'),
    #url(r'^search/$','article.views.blog_search', name = 'search'),
)
