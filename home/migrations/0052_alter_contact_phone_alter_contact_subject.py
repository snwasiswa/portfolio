# Generated by Django 4.0.1 on 2022-01-20 23:32

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0051_remove_portfolio_body_alter_portfolio_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Phone number'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Subject'),
        ),
    ]
