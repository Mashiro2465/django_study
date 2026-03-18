from django.http import Http404
from django.shortcuts import render

from todo.models import ToDo


# Create your views here.
def todo_list(request):
    todos = ToDo.objects.all()
    context = {"todos": todos}
    return render(request, "todo_list.html", context)

def todo_detail(request, todo_id):
    try:
        todo = ToDo.objects.get(pk=todo_id)
    except ToDo.DoesNotExist:
        raise Http404

    context = {"todo": todo}
    return render(request, "todo_info.html", context)

