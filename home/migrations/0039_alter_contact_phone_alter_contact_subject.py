# Generated by Django 4.0.1 on 2022-01-18 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0038_contact_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='0000000000', max_length=10, verbose_name='Phone number'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(default='No subject', max_length=250, verbose_name='Subject'),
        ),
    ]
