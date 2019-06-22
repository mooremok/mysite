from django.shortcuts import render
from django.db.models.aggregates import Count
from . models import Home
from note.views import Note
from blog.views import Blog, Category
from selfsource.views import Book, TecBlog
# Create your views here.

def Index(request):
    #获取首页说明
    purpose = Home.objects.all()
    #获取错误总数、已解决未解决数
    error_count = Note.objects.count()
    status_done = Note.objects.all().filter(notestatus_id='1')
    status_done_count = status_done.count()
    status_not = Note.objects.all().filter(notestatus_id='2')
    status_not_count = status_not.count()
    #获取笔记总数、各分类列表及数量
    blog_count = Blog.objects.count()
    category_count = Category.objects.annotate(num_posts=Count('blog'))
    #获取自学资源
    book_count = Book.objects.count()
    tecblog_count = TecBlog.objects.count()
    #数据字典
    context = {
        'purpose':purpose,
        'error_count':error_count,
        'status_done_count':status_done_count,
        'status_not_count':status_not_count,
        'blog_count':blog_count,
        'category_count':category_count,
        'book_count':book_count,
        'tecblog_count':tecblog_count,
    }

    return render(request, 'index.html', context)

