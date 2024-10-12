# Generated by Django 4.0.1 on 2022-01-19 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0042_alter_mycontacts_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mycontacts',
            name='url',
        ),
        migrations.AddField(
            model_name='mycontacts',
            name='data_or_link',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
