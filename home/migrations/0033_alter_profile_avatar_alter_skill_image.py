# Generated by Django 4.0.1 on 2022-01-15 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_alter_skill_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='images/defaultprofile_vad1ub.png', null=True, upload_to='avatars'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='image',
            field=models.FileField(blank=True, default='images/default-thumb_dn1xzg.png', null=True, upload_to='logos'),
        ),
    ]
