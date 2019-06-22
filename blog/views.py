from django.shortcuts import render
from . models import Tags, Category, Blog
import markdown
from django.db.models.aggregates import Count
import random
# Create your views here.

#显示分类、标签及其数量
def CategoryList(request):
    get_count = Category.objects.annotate(num_posts=Count('blog'))
    get_tags = Tags.objects.annotate(num_posts=Count('blog')).filter(num_posts__gt=0)
    all_in_one = Blog.objects.all()
    get_new_blog = all_in_one.order_by('-created_time')[:15]
    get_hot_blog = all_in_one.order_by('-views')[:15]

    #随机文章
    def random_blogs(except_id=0):
        random_count = 15
        return Blog.objects.exclude(id=except_id).order_by('?')[:random_count]
    get_rand_blog = random_blogs()
    context = {
        'get_count':get_count,
        'get_tags':get_tags,
        'get_new_blog':get_new_blog,
        'get_hot_blog':get_hot_blog,
        'get_rand_blog':get_rand_blog, 
    }
    return render(request, 'blog/category_list.html', context)


#分类标题列表
def BlogList(request, cate_pk):
    titles = Blog.objects.all().filter(category_id=cate_pk).order_by('-created_time')
    #获取文章分类
    cate = Category.objects.get(id=cate_pk)
    #获取分类下的views并升序
    lessviews = titles.order_by('views')[0:9]
    context = {
        'titles':titles,
        'cate':cate,
        'lessviews':lessviews,
    }
    return render(request, 'blog/blog_list.html', context)

#Blog详情
def BlogDetail(request, blog_pk):
    blog = Blog.objects.get(pk=blog_pk)
    blog.content = markdown.markdown(blog.content.replace("\r\n", '  \n'), extensions=[
                                        'markdown.extensions.extra',
                                        'markdown.extensions.codehilite',
                                        'markdown.extensions.toc',
                                        ], safe_mode=True,enable_attributes=False)
    blog.views_in()
    #获取当前文章的所有标签
    tags = blog.tag.all()
    context = {
        'blog':blog,
        'tags':tags,
    }
    return render(request, 'blog/blog_detail.html' ,context)

#标签列表
def TagList(request, tags_pk):
    tags_list = Tags.objects.get(pk=tags_pk)
    blog_name = tags_list.blog_set.all()
    get_tags = Tags.objects.annotate(num_posts=Count('blog')).filter(num_posts__gt=0)
    context = {
        'tags_list':tags_list,
        'blog_name':blog_name,
        'get_tags':get_tags,
    }
    return render(request, 'blog/tags_list.html', context)