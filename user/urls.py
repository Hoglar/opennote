from django.urls import path

from . import views

app_name = "user"
urlpatterns = [
    path("messages/", views.messages, name="messages"),
    path("messageuser/<str:receiver>", views.message_user, name="message_user")
]