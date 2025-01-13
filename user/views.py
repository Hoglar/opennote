from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import MessageForm

# Create your views here.

@login_required
def messages(request):
    pass
    # Messages is a simple site, you get a blank page, with threads in the middle.
    # On thread for each indivudual who has sendt you a message.
    # If one sends more messages, and your returns gets saved in there.
    # Then we only sort on time. 

    return render(request, "user/messages.html")


@login_required
def message_user(request, receiver):
    pass
    print(receiver, "We got it!")
    # Plan is to make a separate site to message users. Else, you can just use the comments
    # Making a simple form, with a text field, max text 512. 
    # Need an user field, that get autofilled, but maybe we can get into same function without
    form = MessageForm
    context = {
        "form": form
    }
    return render(request, "user/messageuser.html", context)