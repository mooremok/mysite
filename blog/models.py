
from django.db import models
from django.contrib.auth.models import User
from mdeditor.fields import MDTextField
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField('分类', max_length=30)

    def __str__(self):
        return '{}'.format(self.name)
    
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

class Tags(models.Model):
    name = models.CharField('标签', max_length=40)

    def __str__(self):
        return '{}'.format(self.name)
    
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

class Blog(models.Model):
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.DO_NOTHING)
    tag = models.ManyToManyField(Tags, verbose_name='标签')
    title = models.CharField('标题', max_length=100)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    content = MDTextField('内容')
    views = models.PositiveIntegerField('阅读量', default=0)

    def __str__(self):
        return '{}'.format(self.title)
    
    def views_in(self):
        self.views += 1
        self.save(update_fields=['views'])
    
    class Meta:
        verbose_name = '博客文章'
        verbose_name_plural = verbose_name
    
    def get_absolute_url(self):
        return reverse('blog:blogdetail', kwargs={'blog_pk':self.pk})