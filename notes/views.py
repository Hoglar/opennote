from django.shortcuts import render, redirect, get_object_or_404
from .forms import NoteForm, OverviewFilter, CommentForm, HelpDescriptionForm
from .models import Categories, Note, Comment, HelpRequests
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F

from notes.view_ex.get_note import get_note
from notes.view_ex.filter_overview import filter_overview

# Create your views here.


@login_required
def create(request):
    if request.method == "POST":
        # First we do category, check if it is in database, else we save it. save id for later
        note = save_note(request)

        return redirect("notes:edit", note.slug)
    else:
        form = NoteForm()

    return render(request, "notes/create.html", {
        "form": form,
        "categories": Categories.objects.all()

    })
# Need to have some sort of filter here, need based on author. category, words
def overview(request):
    if request.method == "POST":

        note_list = filter_overview(request)
        overviewFilter = OverviewFilter(request.POST)

    else:
        note_list = Note.objects.all()[:30]
        overviewFilter = OverviewFilter

    return render(request, "notes/overview.html", {
        "notes": note_list,
        "overviewFilter": overviewFilter
    })

def note(request, note_slug=None):
    if note_slug is None:
        return redirect("notes:overview")
    else:
        # We get object
        try:
            noteObject = Note.objects.get(slug=note_slug)
            comments = Comment.objects.filter(note=noteObject)

            if noteObject.author == request.user:
                return redirect("notes:edit", note_slug)
            noteObject.views = F('views') + 1
            noteObject.save()
            noteObject = get_note(note_slug)

        except ObjectDoesNotExist:
            return redirect("notes:overview")
        
    try:
        help_request = HelpRequests.objects.get(note=get_note(note_slug))
        help_description_form = HelpDescriptionForm(
            initial={"description": help_request.description, "offer": help_request.offer})

        help_description_form.fields["description"].widget.attrs["disabled"] = "disabled"
        help_description_form.fields["offer"].widget.attrs["disabled"] = "disabled"
        


    except ObjectDoesNotExist:
        help_description_form = None   

    return render(request, "notes/note.html", {
        "title": noteObject.title,
        "category": noteObject.category,
        "note": noteObject.note,
        "author": noteObject.author,
        "views": noteObject.views,
        "note_slug": note_slug,
        "commentForm": CommentForm,
        "comments": comments,
        "helpDescriptionForm": help_description_form
    })

def edit(request, note_slug):

    # Need to make this in case of linking to edit page i guess
    if not request.user.is_authenticated:
        return redirect("notes:note", note_slug)
    else:
        # In edit, we may first get the note fra database

        if request.method == "POST":
            # can i do something like this
            noteObject = get_note(note_slug)

            if noteObject.author == request.user:

                noteObject.note = request.POST["note"]
                noteObject.save()
                form = NoteForm({
                        'title': noteObject.title,
                        'category': noteObject.category,
                        'note': noteObject.note
                    })
            else:
                return redirect("notes:note", note_slug)

        else:
            try:
                noteObject = Note.objects.get(slug=note_slug)
                #need to fix this. Thats next
                form = NoteForm({
                    'title': noteObject.title,
                    'category': noteObject.category,
                    'note': noteObject.note
                })
            except ObjectDoesNotExist:
                #Should i maybe throw an error here to inform user page does not exist?
                return redirect("notes:overview")
    

    # Getting help request
    
    try:
        help_request = HelpRequests.objects.get(note=get_note(note_slug))
        help_description_form = HelpDescriptionForm(
            initial={"description": help_request.description, "offer": help_request.offer})
    except ObjectDoesNotExist:
        help_description_form = HelpDescriptionForm()
        
    return render(request, "notes/edit.html", {
        "form": form,
        "title": noteObject.title,
        "category": noteObject.category,
        "note_slug": note_slug,
        "comments": Comment.objects.filter(note=noteObject),
        "commentForm": CommentForm,
        "helpDescriptionForm": help_description_form,
        "views": noteObject.views

    })

@login_required
def delete(request, note_slug):
    note = get_object_or_404(Note, slug=note_slug)
    
    if note.author != request.user:
        return redirect("landingpage:landingpage")

    if request.method == "POST":
        note.delete()
        return redirect("notes:overview")
    
    return redirect("notes:edit", note_slug)

def save_note(request, note_slug=None):
    form = NoteForm(request.POST)
    if form.is_valid():

            category_name = form.cleaned_data["category"]
            category, created = Categories.objects.get_or_create(name=category_name)

            if note_slug is None:
                note = Note(
                    title=form.cleaned_data["title"],
                    category=category,
                    note=form.cleaned_data["note"],
                    author=request.user
                )

            else:
                note = Note.objects.get(slug=note_slug)
                note.note = form.cleaned_data["note"]

            note.save()
            return note

@login_required    
def add_comment(request, note_slug):
    # We need to create a form field, textarea i guess. make it petite, place it under.
    # Maybe its time to bring out the javascript 
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data["comment"]
            note = get_note(note_slug)

            new_comment = Comment(
                comment=comment,
                note=note,
                author=request.user
            )
            new_comment.save()
            
    return redirect("notes:note", note_slug=note_slug)

@login_required
def add_help_request(request, note_slug):
    if request.method == "POST":
        form = HelpDescriptionForm(request.POST)
        if form.is_valid():

            # first see if help request exists? then just add to it. 

            try:
                help_request = HelpRequests.objects.get(note=get_note(note_slug))
            except HelpRequests.DoesNotExist:
                
                help_request = HelpRequests.objects.create(
                    author=request.user,
                    note=Note.objects.get(slug=note_slug),
                    offer=form.cleaned_data["offer"],
                    description=form.cleaned_data["description"]
                )

            else:
                help_request.offer = form.cleaned_data["offer"]
                help_request.description = form.cleaned_data["description"]
                help_request.save()

    return redirect("notes:edit", note_slug=note_slug)
# What does this function need to do. About the same as add comment i guess
#   
