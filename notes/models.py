from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import random
import string

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f"{self.name}"

class Note(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    title = models.CharField(max_length=64, blank=True)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True, related_name="notes")
    note = models.TextField()
    creation_time = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    

    def __str__(self):
        return f"{self.title}, {self.category}"
    
    def save(self, *args, **kwargs):
        if not self.id:
            if not self.slug:
                category_slug = slugify(self.category)
                title_words = [word for word in self.title.split() if word.lower() not in ['and', 'the', 'of']]
                title_slug = slugify(' '.join(title_words))
                random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
                self.slug = f"{category_slug}-{title_slug}-{random_string}"
            else:
                saved_note = Note.objects.get(id=self.id)
                self.slug = saved_note.slug
                self.title = saved_note.title


        super(Note, self).save(*args, **kwargs)
    
class Comment(models.Model):
    comment = models.CharField(max_length=512)
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    creation_time = models.DateTimeField(auto_now_add=True)

class HelpRequests(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="helpRequests")
    note = models.OneToOneField(Note, on_delete=models.CASCADE, related_name="helpRequests")
    offer = models.CharField(max_length=10, blank=True)
    description = models.CharField(max_length=256, blank=True)