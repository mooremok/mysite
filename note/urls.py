from django.urls import path
from . views import NoteList, NoteDetail

#namespace
app_name='note'

urlpatterns = [
    path('', NoteList, name='notelist'),
    path('detail/<int:note_pk>', NoteDetail, name='notedetail'),

]