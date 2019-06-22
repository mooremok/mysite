from django.urls import path
from . views import SourcePage

app_name = 'selfsource'
urlpatterns = [
    path('', SourcePage, name='source'),
]