"""
admin.py

Registers models to the Django admin interface and customizes their appearance and behavior.
Includes integration with TinyMCE for rich text fields and inline field customization for
related models.

Models registered:
- Profile, Contact, Image, Video, Education, Leadership, Experience, Course, Skill,
  MyContact, Portfolio
"""

from django.contrib import admin
from django import forms
from tinymce.widgets import TinyMCE
from .models import (
    Leadership, Profile, Contact, Feedback, ProjectImage,
    Education, Skill, Portfolio, Course, MyContact, Video, Experience,
)

# -------------------------------
# Contact Admin
# -------------------------------

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Admin configuration for Contact model.
    """
    list_display = ('id', 'name', 'email', 'timestamp')


# -------------------------------
# Profile Admin
# -------------------------------

class ProfileAdminForm(forms.ModelForm):
    """
    Custom form for Profile admin to enable TinyMCE on the biography field.
    """
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'biography': TinyMCE(attrs={'cols': 80, 'rows': 30}),
            'welcome_summary': TinyMCE(attrs={'cols': 80, 'rows': 30}),
            'intro_summary': TinyMCE(attrs={'cols': 80, 'rows': 30}),
            'resume_summary': TinyMCE(attrs={'cols': 80, 'rows': 30}),
            'academic_projects_summary': TinyMCE(attrs={'cols': 80, 'rows': 30}),
            'side_projects_summary': TinyMCE(attrs={'cols': 80, 'rows': 30}),
            'contact_summary': TinyMCE(attrs={'cols': 80, 'rows': 30}),
        }


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for Profile model with horizontal filters.
    """
    form = ProfileAdminForm
    list_display = ('id', 'user')
    filter_horizontal = ('experiences', 'educations', 'skills', 'courses', 'projects', 'leaderships', 'links')


# -------------------------------
# Video Admin
# -------------------------------

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    """
    Admin configuration for Video model.
    """
    list_display = ('id', 'name')


# -------------------------------
# Education Admin
# -------------------------------

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    """
    Admin configuration for Education model.
    """
    list_display = ('id', 'degree', 'school', 'major')


# -------------------------------
# Portfolio/Project Image Admin
# -------------------------------

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    """
    Admin configuration for ProjectImage model.
    """
    list_display = ('portfolio', 'image', 'url')

# -------------------------------
# Leadership Admin
# -------------------------------

class LeadershipAdminForm(forms.ModelForm):
    """
    Custom form for Leadership admin with TinyMCE.
    """
    class Meta:
        model = Leadership
        fields = '__all__'
        widgets = {
            'description': TinyMCE(attrs={'cols': 80, 'rows': 30}),
        }

@admin.register(Leadership)
class LeadershipAdmin(admin.ModelAdmin):
    """
    Admin configuration for Leadership model.
    """
    form = LeadershipAdminForm
    list_display = ('id', 'name')


# -------------------------------
# Experience Admin
# -------------------------------

class ExperienceAdminForm(forms.ModelForm):
    """
    Custom form for Experience admin with TinyMCE.
    """
    class Meta:
        model = Experience
        fields = '__all__'
        widgets = {
            'description': TinyMCE(attrs={'cols': 80, 'rows': 30}),
        }

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    """
    Admin configuration for Experience model.
    """
    form = ExperienceAdminForm
    list_display = ('id', 'job_title', 'company_name')


# -------------------------------
# Course Admin
# -------------------------------

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """
    Admin configuration for Course model.
    """
    list_display = ('id', 'name')


# -------------------------------
# Skill Admin
# -------------------------------

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """
    Admin configuration for Skill model.
    """
    list_display = ('id', 'name', 'rating')


# -------------------------------
# MyContact Admin
# -------------------------------

@admin.register(MyContact)
class MyContactAdmin(admin.ModelAdmin):
    """
    Admin configuration for MyContact model.
    """
    list_display = ('id', 'name', 'category')


# -------------------------------
# Portfolio Admin
# -------------------------------

class PortfolioAdminForm(forms.ModelForm):
    """
    Custom form for Portfolio admin with TinyMCE on the body field.
    """
    class Meta:
        model = Portfolio
        fields = '__all__'
        widgets = {
            'body': TinyMCE(attrs={'cols': 80, 'rows': 30}),
        }

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    """
    Admin configuration for Portfolio model.
    """
    form = PortfolioAdminForm
    list_display = ('id', 'name', 'is_active', 'year')
    readonly_fields = ('slug',)
