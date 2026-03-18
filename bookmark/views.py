from django.http import Http404
from django.shortcuts import render

from bookmark.models import Bookmark


def bookmark_list(request):
    bookmarks = Bookmark.objects.all()
    context = {'bookmarks': bookmarks}
    return render(request, "bookmark_list.html", context)

def bookmark_detail(request, pk):
    try:
        bookmark = Bookmark.objects.get(pk=pk)
    except Bookmark.DoesNotExist:
        raise Http404

    context = {'bookmark':bookmark}
    return render(request, "bookmark_detail.html", context)