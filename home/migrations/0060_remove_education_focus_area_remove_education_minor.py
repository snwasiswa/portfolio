# Generated by Django 5.1.1 on 2024-10-11 00:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0059_education_major_education_minor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='focus_area',
        ),
        migrations.RemoveField(
            model_name='education',
            name='minor',
        ),
    ]
