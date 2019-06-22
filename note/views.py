from django.shortcuts import render
from . models import Note, NoteType
import markdown
# Create your views here.

#note列表页
def NoteList(request):
    notelist = Note.objects.all().order_by('-created_time')
    count_all = Note.objects.count()
    status_filter = notelist.filter(notestatus_id='2')
    count_filter = status_filter.count()
    context = {
        'notelist':notelist,
        'count_all':count_all,
        'count_filter':count_filter
    }
    return render(request, 'note/note_list.html', context)

def NoteDetail(request, note_pk):
    notedetail = Note.objects.get(pk=note_pk)
    notedetail.erinfo = markdown.markdown(notedetail.erinfo.replace("\r\n", '  \n'), extensions=[
                                        'markdown.extensions.extra',
                                        'markdown.extensions.codehilite',
                                        'markdown.extensions.toc',
                                        ], safe_mode=True,enable_attributes=False)
    notedetail.res_for = markdown.markdown(notedetail.res_for.replace("\r\n", '  \n'), extensions=[
                                        'markdown.extensions.extra',
                                        'markdown.extensions.codehilite',
                                        'markdown.extensions.toc',
                                        ], safe_mode=True,enable_attributes=False)
    notedetail.veiws_increase()
    #侧边栏遍历
    #获取当前分类的id
    notetype_id = notedetail.notetype_id
    #获得当前分类下的所有文章标题
    note_title = Note.objects.all().filter(notetype_id=notetype_id)
    context = {
        'notedetail':notedetail,
        'notetype_id':notetype_id,
        'note_title':note_title,
    }
    return render(request, 'note/note_detail.html', context)