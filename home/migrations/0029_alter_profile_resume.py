# Generated by Django 4.0.1 on 2022-01-07 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_alter_contact_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='resume',
            field=models.FileField(blank=True, default=None, null=True, upload_to='resumes'),
        ),
    ]
