"""
models.py

Defines the data models for the portfolio web application.
Includes user profiles, education, experience, projects, skills,
contacts, media (images/videos), and feedback.

Each model typically relates to the `Profile` model to support a dynamic user resume system.
"""

import os
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField
from tinymce.models import HTMLField
from django.contrib.auth.hashers import make_password, check_password
from cloudinary_storage.storage import MediaCloudinaryStorage


# ==========================
# Education Model
# ==========================

class Education(models.Model):
    """Model to store educational background"""
    degree = models.CharField(blank=True, null=True, max_length=250)
    school = models.CharField(blank=True, null=True, max_length=250)
    major = models.CharField(blank=True, null=True, max_length=250)
    minor = models.CharField(blank=True, null=True, max_length=250)
    focus_area = models.CharField(blank=True, null=True, max_length=250)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(blank=True, null=True)
    year = models.CharField(blank=True, null=True, max_length=100)
    description = models.CharField(blank=True, null=True, max_length=250)
    profiles = models.ManyToManyField('Profile', related_name='all_educations')

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'

    def __str__(self):
        return self.degree or "Unnamed Education"


# ==========================
# Skill Model
# ==========================

class Skill(models.Model):
    """Model to store skills and their attributes"""
    name = models.CharField(max_length=25, blank=True, null=True)
    image = models.FileField(upload_to="logos", storage=MediaCloudinaryStorage(), null=True, blank=True)
    rating = models.IntegerField(default=4, null=True, blank=True)
    is_key_skill = models.BooleanField(default=False)
    is_hard_skill = models.BooleanField(default=False)
    is_soft_skill = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    category = models.CharField(max_length=70, blank=True, null=True)
    profiles = models.ManyToManyField('Profile', related_name='all_skills')

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name or "Unnamed Skill"

    @property
    def get_logo_url(self):
        """Returns logo URL or a default image"""
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        return "https://res.cloudinary.com/dh13i9dce/image/upload/v1642216413/media/logos/default-thumb_dn1xzg.png"


# ==========================
# Course Model
# ==========================

class Course(models.Model):
    """Model to store completed or current courses"""
    name = models.CharField(blank=True, null=True, max_length=100)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(blank=True, null=True, max_length=250)
    profiles = models.ManyToManyField('Profile', related_name='all_courses')

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.name or "Unnamed Course"


# ==========================
# Leadership Model
# ==========================

class Leadership(models.Model):
    """Model for campus involvement or leadership experience"""
    name = models.CharField(blank=True, null=True, max_length=500)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(blank=True, null=True)
    description = HTMLField()
    profiles = models.ManyToManyField('Profile', related_name='all_leaderships')

    class Meta:
        verbose_name = 'Leadership'
        verbose_name_plural = 'Leaderships'

    def __str__(self):
        return self.name or "Unnamed Leadership"


# ==========================
# MyContact Model
# ==========================

class MyContact(models.Model):
    """Model to store user’s external links (e.g. LinkedIn, GitHub)"""
    name = models.CharField(blank=True, null=True, max_length=250)
    data = models.CharField(blank=True, null=True, max_length=250)
    icon = models.ImageField(blank=True, null=True, storage=MediaCloudinaryStorage(), upload_to="images")
    category = models.CharField(blank=True, null=True, max_length=250)
    is_active = models.BooleanField(default=True)
    url = models.URLField(blank=True, null=True)
    profiles = models.ManyToManyField('Profile', related_name='all_links')

    class Meta:
        verbose_name = 'MyContact'
        verbose_name_plural = 'MyContacts'
        ordering = ["name"]

    def __str__(self):
        return self.name or "Unnamed Contact"

    @property
    def get_icon_url(self):
        """Returns icon URL or a default icon"""
        if self.icon and hasattr(self.icon, 'url'):
            return self.icon.url
        return "https://res.cloudinary.com/dh13i9dce/image/upload/v1642216413/media/logos/default-thumb_dn1xzg.png"


# ==========================
# Portfolio Model
# ==========================

class Portfolio(models.Model):
    """Model to store project/portfolio items"""
    name = models.CharField(blank=True, null=True, max_length=250)
    image = models.ImageField(blank=True, null=True, storage=MediaCloudinaryStorage(), upload_to="portfolios")
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(null=True, blank=True)
    description = models.CharField(blank=True, null=True, max_length=250)
    body = HTMLField()
    date = models.DateTimeField(blank=True, null=True)
    is_side_project = models.BooleanField(null=True, blank=True)
    for_resume = models.BooleanField(default=False)
    url = models.URLField(null=True, blank=True)
    year = models.CharField(blank=True, null=True, max_length=70)
    technology = models.JSONField(blank=True, null=True)
    profiles = models.ManyToManyField('Profile', related_name='all_projects')

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolios'
        ordering = ["name"]

    def __str__(self):
        return self.name or "Unnamed Project"

    def save(self, *args, **kwargs):
        """Generate slug if missing"""
        if not self.id:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f"/portfolio/{self.slug}"

    @property
    def get_logo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        return "https://res.cloudinary.com/dh13i9dce/image/upload/v1642216413/media/logos/default-thumb_dn1xzg.png"


# ==========================
# Experience Model
# ==========================

class Experience(models.Model):
    """Model to represent job experience"""
    job_title = models.CharField(max_length=250)
    company_name = models.CharField(max_length=250)
    location = models.CharField(max_length=250, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    description = HTMLField()
    profiles = models.ManyToManyField('Profile', related_name='all_experiences')

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"


# ==========================
# Profile Model
# ==========================

class Profile(models.Model):
    """Model for a user's portfolio profile"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, blank=True, null=True)
    biography = HTMLField(default="Passionate about building clean, scalable software that solves real-world problems.")
    avatar = models.ImageField(blank=True, null=True, storage=MediaCloudinaryStorage(),upload_to="avatars")
    resume = models.FileField(blank=True, null=True, storage=MediaCloudinaryStorage(), upload_to="resumes")
    resume_password = models.CharField(max_length=255, blank=True, null=True)
    work = models.FileField(blank=True, null=True, storage=MediaCloudinaryStorage(), upload_to="work_samples")
    welcome_summary = HTMLField(default="My passion...")
    intro_summary = HTMLField(default="Passionate about building clean, scalable solutions.")
    resume_summary = HTMLField(default="A quick overview of my experience, skills, and education.")
    academic_projects_summary = HTMLField(
        default="Projects built during my studies, focused on applying core concepts.")
    side_projects_summary = HTMLField(default="Independent work exploring new tools and solving real problems.")
    contact_summary = HTMLField(default="Let’s connect — I’m open to opportunities, ideas, or questions.")
    courses = models.ManyToManyField(Course, blank=True)
    leaderships = models.ManyToManyField(Leadership, blank=True)
    skills = models.ManyToManyField(Skill, blank=True)
    projects = models.ManyToManyField(Portfolio, blank=True)
    links = models.ManyToManyField(MyContact, blank=True)
    educations = models.ManyToManyField(Education, blank=True)
    experiences = models.ManyToManyField(Experience, blank=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def set_resume_password(self, password: str):
        """Hashes and sets a password for resume access"""
        self.resume_password = make_password(password)

    def check_resume_password(self, password: str) -> bool:
        """Verifies the provided password against stored hash"""
        return check_password(password, self.resume_password)

    def save(self, *args, **kwargs):
        if self.resume_password:
            self.resume_password = make_password(self.resume_password)
        super().save(*args, **kwargs)

    @property
    def get_resume_url(self):
        if self.resume and hasattr(self.resume, 'url'):
            return self.resume.url
        return "https://res.cloudinary.com/dh13i9dce/image/upload/v1657859552/media/resumes/online_resume_kn1apo.pdf"

    @property
    def get_work_samples_url(self):
        if self.work and hasattr(self.work, 'url'):
            return self.work.url
        return "https://res.cloudinary.com/dh13i9dce/image/upload/v1657859552/media/resumes/online_resume_kn1apo.pdf"

    @property
    def get_avatar_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        return "https://res.cloudinary.com/dh13i9dce/image/upload/v1642216377/media/avatars/defaultprofile_vad1ub.png"


# ==========================
# Contact Model
# ==========================

class Contact(models.Model):
    """Model for website contact form submissions"""
    name = models.CharField(verbose_name="Name", max_length=250)
    email = models.CharField(verbose_name="Email", max_length=250)
    message = models.TextField(verbose_name="Message", max_length=2000)
    phone = PhoneNumberField(verbose_name="Phone number", blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(verbose_name="Subject", max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return f"{self.name} ({self.email})"


# ==========================
# Feedback Model
# ==========================

class Feedback(models.Model):
    """Model for testimonial or feedback quotes"""
    name = models.CharField(blank=True, null=True, max_length=250)
    role = models.CharField(blank=True, null=True, max_length=250)
    quote = models.CharField(blank=True, null=True, max_length=250)
    thumbnail = models.ImageField(blank=True, null=True, upload_to="feedbacks")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'
        ordering = ["name"]

    def __str__(self):
        return self.name or "Unnamed Feedback"

    @property
    def get_thumbnail_url(self):
        if self.thumbnail and hasattr(self.thumbnail, 'url'):
            return self.thumbnail.url
        return "https://res.cloudinary.com/dh13i9dce/image/upload/v1642216413/media/logos/default-thumb_dn1xzg.png"


# ==========================
# Image Model
# ==========================

class ProjectImage(models.Model):
    """Model for images associated with a project/portfolio item"""
    portfolio = models.ForeignKey(
        'Portfolio',
        on_delete=models.CASCADE,
        related_name='images'
    )
    name = models.CharField(blank=True, null=True, max_length=250)
    url = models.URLField(blank=True, null=True)
    image = models.ImageField(
        blank=True,
        null=True,
        storage=MediaCloudinaryStorage(),
        upload_to="projects"
    )
    is_image = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Project Image'
        verbose_name_plural = 'Project Images'
        ordering = ["name"]

    def save(self, *args, **kwargs):
        # If URL exists, mark this as not an uploaded image
        if self.url:
            self.is_image = False
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name or f"Image for {self.portfolio.name}"

    @property
    def get_image_url(self):
        # Return image URL if exists, else default placeholder
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        return "https://res.cloudinary.com/dh13i9dce/image/upload/v1642216413/media/logos/default-thumb_dn1xzg.png"

# ==========================
# Video Model
# ==========================

def validate_video_file_extension(value):
    """Restrict upload to common video formats"""
    ext = os.path.splitext(value.name)[1]
    if ext.lower() not in ['.mp4', '.avi', '.mov', '.mkv']:
        raise ValidationError('Unsupported video file extension.')


class Video(models.Model):
    """Model for uploaded videos"""
    name = models.CharField(max_length=100)
    url = models.URLField(blank=True, null=True)
    video_file = models.FileField(upload_to='videos/', storage=MediaCloudinaryStorage(),
                                  validators=[validate_video_file_extension])
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_video = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
        ordering = ["name"]

    def save(self, *args, **kwargs):
        if self.url:
            self.is_video = False
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name or "Unnamed Video"

    @property
    def get_video_url(self):
        if self.video_file and hasattr(self.video_file, 'url'):
            return self.video_file.url
        return ""
