# Generated by Django 4.2.3 on 2023-08-11 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0007_note_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='slug',
        ),
    ]
