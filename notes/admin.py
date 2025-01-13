from django.contrib import admin
from .models import Note, Categories, Comment, HelpRequests
# Register your models here.

admin.site.register(Note)
admin.site.register(Categories)
admin.site.register(Comment)
admin.site.register(HelpRequests)

