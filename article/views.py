# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.http import Http404
from markdown import markdown

# Create your views here.
#def home(request):
#    return HttpResponse("Hello World, Django")

def home(request):
    post_list = Article.objects.all()  #获取全部的Article对象
    return render(request, 'home.html', {'post_list' : post_list})

#def detail(request, my_args):
#    #return HttpResponse("You're looking at my_args %s." %my_args)

#    post = Article.objects.all()[int(my_args)]
#    str = ("title = %s, category = %s, date_time = %s, content = %s" % (post.title, post.category, post.date_time, post.content))
#    return HttpResponse(str)

def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
        #post.content = markdown(post.content,['codehilite'])
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post' : post})

#def test(request):
#    return render(request, 'test.html', {'current_time': datetime.now()})

def archives(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'archives.html', {'post_list' : post_list, 
                                            'error' : False})
def about_me(request):
    return render(request, 'aboutme.html')

def search_tag(request, tag):
    try:
        post_list = Article.objects.filter(category__iexact = tag) #contains
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'tag.html', {'post_list' : post_list})
