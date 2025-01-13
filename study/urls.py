from django.urls import path
from . import views

app_name = "study"
urlpatterns = [
    path("plan/", views.plan, name="plan"),
    path("createtask/", views.create_task, name="create_task")
]