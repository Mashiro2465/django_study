from gc import get_objects

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from todo.forms import ToDoForm, ToDoUpdateForm
from todo.models import ToDo


@login_required()
def todo_list(request):
    todos = ToDo.objects.filter(user=request.user).order_by("-created_at")
    q = request.GET.get("q")
    if q:
        todos = todos.filter(Q(title__icontains=q) | Q(description__icontains=q))
    paginator = Paginator(todos, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj
    }
    return render(request, "todo/todo_list.html", context)

@login_required()
def todo_info(request, todo_id):
    todo = get_object_or_404(ToDo, id=todo_id, user=request.user)
    context = {
        "todo" : todo.__dict__
    }
    return render(request, "todo/todo_info.html", context)

@login_required()
def todo_create(request):
    form = ToDoForm(request.POST or None)
    if form.is_valid():
        todo = form.save(commit=False)
        todo.user = request.user
        todo.save()
        return redirect(reverse('todo_info', kwargs={'todo_id': todo.pk}))

    context = {
        "form": form
    }
    return render(request, "todo/todo_create.html", context)

@login_required()
def todo_update(request, todo_id):
    todo = get_object_or_404(ToDo, id=todo_id, user = request.user)
    form = ToDoUpdateForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect(reverse('todo_info', kwargs={'todo_id': todo.pk}))

    context = {
        "form": form
        }

    return render(request, "todo/todo_update.html", context)

@login_required()
@require_http_methods(["POST"])
def todo_delete(request, todo_id):
    todo = get_object_or_404(ToDo, id=todo_id, user = request.user)
    todo.delete()
    return redirect(reverse('todo_list'))
