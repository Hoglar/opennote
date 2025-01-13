from django.urls import path

from . import views

app_name = "notes"
urlpatterns = [
    path("edit/<str:note_slug>", views.edit, name="edit"),
    path("overview/", views.overview, name="overview"),
    path("note/", views.note, name="note"),
    path("note/<str:note_slug>", views.note, name="note"),
    path("create/", views.create, name="create"),
    path("delete/<str:note_slug>", views.delete, name="delete"),
    path("addcomment/<str:note_slug>", views.add_comment, name="add_comment"),
    path("add_help_request/<str:note_slug>", views.add_help_request, name="add_help_request")
]