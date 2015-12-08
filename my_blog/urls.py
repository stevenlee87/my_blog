# coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin

#千万不能写成from my_blog.article import views as articleviews,这样会找不到article app
from article import views as articleviews
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', articleviews.home),
    #url(r'^$', article.views.home),
    url(r'^(?P<my_args>\d+)/$', articleviews.detail, name='detail'),
    #url(r'^test/$', articleviews.test),
)
