# Generated by Django 4.0.1 on 2023-05-25 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0056_profile_work_alter_profile_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycontacts',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='icons'),
        ),
    ]
