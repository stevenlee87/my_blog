# coding:utf-8
from django.db import models
from django.core.urlresolvers import reverse


class Article(models.Model):  # Create your models here.
    title = models.CharField(max_length=100)  # blog tile
    category = models.CharField(max_length=50, blank=True)  # blog category
    date_time = models.DateTimeField(auto_now_add=True)  # blog datetime
    content = models.TextField(blank=True, null=True)  # blog content

    # 获取URL并转换成url的表示格式
    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id': self.id})
        return "http://192.168.147.133:8000%s" % path

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']
