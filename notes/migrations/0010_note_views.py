# Generated by Django 4.2.3 on 2023-08-12 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0009_note_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
