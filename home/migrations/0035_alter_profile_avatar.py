# Generated by Django 4.0.1 on 2022-01-15 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_alter_profile_avatar_alter_skill_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars'),
        ),
    ]