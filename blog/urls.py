from django.urls import path
from . views import CategoryList, BlogList, BlogDetail, TagList

#namespace
app_name = 'blog'

urlpatterns = [
    path('', CategoryList, name='categorylist'),
    path('list/cid/<cate_pk>', BlogList, name='bloglist'),
    path('detail/<blog_pk>', BlogDetail, name='blogdetail'),
    path('taglist/<tags_pk>', TagList, name='taglist'),
]
