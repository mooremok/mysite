from django.shortcuts import render
from . models import Book, TecBlog, Collection
# Create your views here.

def SourcePage(request):
    books = Book.objects.all()
    sites = TecBlog.objects.all()
    colles = Collection.objects.all()
    context = {
        'books':books,
        'sites':sites,
        'colles':colles,
    }
    return render(request, 'selfsource/source.html', context)