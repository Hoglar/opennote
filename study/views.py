from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def plan(request):
    name = "Billy"

    return render(request, "study/plan.html", {
        "name": name
    })

@login_required
def create_task(request):
    if request.method == "POST":
        print("Hello")