# Generated by Django 4.0.1 on 2022-03-12 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0056_alter_profile_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resumes'),
        ),
    ]