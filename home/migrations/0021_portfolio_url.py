# Generated by Django 4.0 on 2021-12-23 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_alter_portfolio_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
