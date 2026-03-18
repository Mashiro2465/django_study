"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render
from bookmark import views
from todo import views as todo_views

game_list = [
    {"title": "로스트아크", "company": "스마일 게이트"},
    {"title": "메이플스토리", "company": "넥슨"}
]


def index(request):
    return HttpResponse("Hello, world.")

def book_list(request):


    return render(request, "book_list.html", {"range": range(0,10)})

def book(request, num):
    return render(request, "book_detail.html", {"num": num})

def language(request, lang):
    return HttpResponse(f"<h1>{lang} 언어 페이지 입니다.</h1>")

def games(request):
    game_titles = [game["title"] for game in game_list]
    response_text = "<br>".join(game_titles)
    return render(request, "games.html", {"game_list": game_list})

def game_detail(request, index):
    game = game_list[index]

    return render(request, "game.html", {"game": game})

def gugu(request):

    return render(request, "gugu.html", {"range": range(2,10)})

def gugu_detail(request, num):

    result = [num * i for i in range(1,10)]

    return render(request, "gugu_detail.html", {"num": num, "result" : result})

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", index),
    # path("book_list/", book_list),
    # path("book_list/<int:num>/", book),
    # path("language/<str:lang>", language),
    # path("game/", games),
    # path("game/<int:index>", game_detail),
    # path("gugu/", gugu),
    # path("gugu/<int:num>/", gugu_detail),
    path("bookmark/", views.bookmark_list),
    path("bookmark/<int:pk>", views.bookmark_detail),
    path("todo/",todo_views.todo_list),
    path("todo/<int:todo_id>/",todo_views.todo_detail),
]
