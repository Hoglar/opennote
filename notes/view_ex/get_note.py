from ..models import Note
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist



# This function exsist because i often need to get the note object from database
# I usualy do this with note_slugs. so this takes a note_slug and returns a note object
# If slug is faulty, and note does not exist, it redirects to overview


def get_note(note_slug):
    try:
        noteObject = Note.objects.get(slug=note_slug)

    except ObjectDoesNotExist:
                #Should i maybe throw an error here to inform user page does not exist?
        return redirect("notes:overview")
    return noteObject