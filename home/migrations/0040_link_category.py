# Generated by Django 4.0.1 on 2022-01-19 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0039_alter_contact_phone_alter_contact_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='category',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]