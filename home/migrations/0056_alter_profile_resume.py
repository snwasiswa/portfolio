# Generated by Django 4.0.1 on 2022-03-12 16:47

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0055_alter_profile_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='resume',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
    ]
