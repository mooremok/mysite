from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField('书名', max_length=30)
    author = models.CharField('作者', max_length=30)
    lang = models.CharField('语言', max_length=20)
    suit = models.CharField('定位', max_length=30)
    core = models.TextField('概要')
    img = models.ImageField('封面图片', upload_to='source_book')

    class Meta:
        verbose_name = '书籍'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.title

class TecBlog(models.Model):
    site = models.CharField('名称', max_length=20)
    site_url = models.URLField('网址')
    text = models.TextField('说明', blank=True, null=True)

    class Meta:
        verbose_name = '技术博客'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.site

class Collection(models.Model):
    name = models.CharField('名称', max_length=200)
    site_url = models.URLField('网址')
    text = models.TextField('说明', blank=True, null=True)
    coll_time = models.DateTimeField('时间', auto_now_add=True)

    class Meta:
        verbose_name = '收藏'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.name