# Generated by Django 4.0 on 2021-12-22 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_leadership_portfolio_is_side_project_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='leaderships',
            field=models.ManyToManyField(blank=True, to='home.Leadership'),
        ),
    ]
