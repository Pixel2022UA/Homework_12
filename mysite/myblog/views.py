import time
from django.http import HttpResponse
from django.views.decorators.http import condition
from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article

from faker import Faker

fake = Faker()


def add_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect("get_article", id=article.id)
    else:
        initial_data = {
            "title": fake.first_name(),
            "content": fake.text(max_nb_chars=200),
        }
        form = ArticleForm(initial=initial_data)
    context = {"form": form}
    return render(request, "add_article.html", context)


def latest_entry(request, id: int):
    article = Article.objects.filter(id=id).latest("updated_at")
    return article.updated_at


@condition(last_modified_func=latest_entry)
def get_article(request, id: int):
    article = Article.objects.get(id=id)
    time.sleep(3)
    context = {"article": article}
    return render(request, "get_article.html", context)


def edit_article(request, id: int):
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        return HttpResponse(f"Article with this id has not yet been created")

    if request.method == "GET":
        form = ArticleForm(instance=article)
        context = {"form": form}
        return render(request, "edit_article.html", context)

    elif request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect("get_article", id=id)
        else:
            context = {"form": form}
            return render(request, "edit_article.html", context)
