from django.contrib import admin
from .models import Leadership, Profile, Contact, Feedback, Image, Education, Skill, Portfolio, Course, MyContacts


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'timestamp')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'degree', 'school')


@admin.register(Leadership)
class LeadershipAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rating')


@admin.register(MyContacts)
class MyContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'year')
    readonly_fields = ('slug',)
