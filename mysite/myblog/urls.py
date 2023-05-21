from django.urls import path
from . import views

urlpatterns = [
    path("add-article/", views.add_article, name="add_article"),
    path("get-article/<int:id>/", views.get_article, name="get_article"),
    path("edit-article/<int:id>/", views.edit_article, name="edit_article"),
]
