from django.shortcuts import render, HttpResponse
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

def test(request, question_id):
    return HttpResponse(f"you're looking at {question_id}")