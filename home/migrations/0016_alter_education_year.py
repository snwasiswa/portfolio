# Generated by Django 4.0 on 2021-12-22 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_profile_educations_alter_profile_leaderships'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='year',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
