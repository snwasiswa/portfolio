# Generated by Django 4.0 on 2021-12-22 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_course_profile_courses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leadership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('name', models.CharField(blank=True, max_length=70, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name': 'Leadership',
                'verbose_name_plural': 'Leaderships',
            },
        ),
        migrations.AddField(
            model_name='portfolio',
            name='is_side_project',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='is_hard_skill',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='skill',
            name='is_soft_skill',
            field=models.BooleanField(default=False),
        ),
    ]