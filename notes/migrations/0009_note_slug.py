# Generated by Django 4.2.3 on 2023-08-11 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0008_remove_note_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='slug',
            field=models.SlugField(default='undef', unique=True),
            preserve_default=False,
        ),
    ]
