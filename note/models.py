from django.db import models
from django.contrib.auth.models import User
from mdeditor.fields import MDTextField
from django.urls import reverse
# Create your models here.

#notes的状态，分为已解决和未解决
class NoteStatus(models.Model):
    notestatus = models.CharField('状态', max_length=10)

    class Meta:
        verbose_name = '状态'
        verbose_name_plural = '状态'
    
    def __str__(self):
        return '{}'.format(self.notestatus)

#notes的分类
class NoteType(models.Model):
    notetype = models.CharField('错误类型', max_length=30)

    class Meta:
        verbose_name = '错误类型'
        verbose_name_plural = '错误类型'
    
    def __str__(self):
        return '{}'.format(self.notetype)

#django/python版本
class PDVersion(models.Model):
    pdversion = models.CharField('版本', max_length=20)

    class Meta:
        verbose_name = '版本'
        verbose_name_plural = '版本'
    
    def __str__(self):
        return '{}'.format(self.pdversion)

#note
class Note(models.Model):
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    title = models.CharField("标题", max_length=100)
    notetype = models.ForeignKey(NoteType, verbose_name='错误类型', on_delete=models.DO_NOTHING, related_name='note_type')
    pdversion = models.ForeignKey(PDVersion, verbose_name='版本', on_delete=models.DO_NOTHING, related_name='pd_version')
    notestatus = models.ForeignKey(NoteStatus, verbose_name='状态', on_delete=models.DO_NOTHING, related_name='note_status')
    erinfo = MDTextField('错误内容', blank=True, null=True)
    res_for = MDTextField('解决方案')
    created_time = models.DateTimeField('记录时间', auto_now_add=True)
    views = models.PositiveIntegerField('阅读量', default=0)

    class Meta:
        verbose_name = '错误记录'
        verbose_name_plural = '错误记录'
    
    def __str__(self):
        return '{}'.format(self.title)
    
    def veiws_increase(self):
        self.views += 1
        self.save(update_fields=['views'])

    def get_absolute_url(self):
        return reverse('note:notedetail', kwargs={'note_pk':self.pk})