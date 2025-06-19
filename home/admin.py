from django.contrib import admin
from .models import Leadership, Profile, Contact, Feedback, Image, Education, Skill, Portfolio, Course, MyContact, Video, Experience
from django import forms
from tinymce.widgets import TinyMCE

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'timestamp')

class ProfileAdminForm(forms.ModelForm):
    class Meta:
        model = Leadership
        fields = '__all__'
        widgets = {
            'biography': TinyMCE(attrs={'cols': 80, 'rows': 30}),
        }

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    form = ProfileAdminForm
    list_display = ('id', 'user')
    filter_horizontal = ('experiences', 'educations', 'skills', 'courses', 'projects', 'leaderships', 'links')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'degree', 'school', 'major')


class LeadershipAdminForm(forms.ModelForm):
    class Meta:
        model = Leadership
        fields = '__all__'
        widgets = {
            'description': TinyMCE(attrs={'cols': 80, 'rows': 30}),
        }

@admin.register(Leadership)
class LeadershipAdmin(admin.ModelAdmin):
    form = LeadershipAdminForm
    list_display = ('id', 'name')

class ExperienceAdminForm(forms.ModelForm):
    class Meta:
        model = Leadership
        fields = '__all__'
        widgets = {
            'description': TinyMCE(attrs={'cols': 80, 'rows': 30}),
        }

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    form = ExperienceAdminForm
    list_display = ('id', 'job_title', 'company_name')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rating')


@admin.register(MyContact)
class MyContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')

class PortfolioAdminForm(forms.ModelForm):
    class Meta:
        model = Leadership
        fields = '__all__'
        widgets = {
            'body': TinyMCE(attrs={'cols': 80, 'rows': 30}),
        }
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    form = PortfolioAdminForm
    list_display = ('id', 'name', 'is_active', 'year')
    readonly_fields = ('slug',)
