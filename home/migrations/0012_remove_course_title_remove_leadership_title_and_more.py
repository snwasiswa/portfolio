# Generated by Django 4.0 on 2021-12-22 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_profile_leaderships'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='title',
        ),
        migrations.RemoveField(
            model_name='leadership',
            name='title',
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='leadership',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
