from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


# Create your models here.

class Education(models.Model):
    """Model for user certificate"""
    degree = models.CharField(blank=True, null=True, max_length=250)
    school = models.CharField(blank=True, null=True, max_length=250)
    focus_area = models.CharField(blank=True, null=True, max_length=250)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(blank=True, null=True)
    year = models.CharField(blank=True, null=True, max_length=100)
    description = models.CharField(blank=True, null=True, max_length=250)

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'

    def __str__(self):
        return self.degree


class Skill(models.Model):
    """Model for skills"""
    name = models.CharField(max_length=25, blank=True, null=True)
    image = models.FileField(upload_to="logos", null=True, blank=True)
    rating = models.IntegerField(default=4, null=True, blank=True)
    is_key_skill = models.BooleanField(default=False)
    is_hard_skill = models.BooleanField(default=False)
    is_soft_skill = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    category = models.CharField(max_length=70, blank=True, null=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name

    @property
    def get_logo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/media/logos/default-thumb_dn1xzg.png"


class Course(models.Model):
    """Model for user course"""
    name = models.CharField(blank=True, null=True, max_length=100)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(blank=True, null=True, max_length=250)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.name


class Leadership(models.Model):
    """Model for user campus involvement or leadership"""
    name = models.CharField(blank=True, null=True, max_length=500)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(blank=True, null=True, max_length=250)

    class Meta:
        verbose_name = 'Leadership'
        verbose_name_plural = 'Leaderships'

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    """Model for user portfolio"""
    name = models.CharField(blank=True, null=True, max_length=250)
    description = models.CharField(blank=True, null=True, max_length=1000)
    image = models.ImageField(blank=True, null=True, upload_to="portfolios")
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(null=True, blank=True)
    body = RichTextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    is_side_project = models.BooleanField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    year = models.CharField(blank=True, null=True, max_length=70)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolios'
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/portfolio/{self.slug}"

    @property
    def get_logo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/media/logos/default-thumb_dn1xzg.png"


class Profile(models.Model):
    """Model for the user profile"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatars")
    resume = models.FileField(blank=True, null=True, upload_to="resumes")
    courses = models.ManyToManyField(Course, blank=True)
    leaderships = models.ManyToManyField(Leadership, blank=True)
    educations = models.ManyToManyField(Education, blank=True)
    projects = models.ManyToManyField(Portfolio, blank=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @property
    def get_avatar_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        else:
            return "/media/avatars/defaultprofile_vad1ub.png"


class Contact(models.Model):
    """Model for user contact"""
    name = models.CharField(verbose_name="Name", max_length=250)
    email = models.CharField(verbose_name="Email", max_length=250)
    message = models.TextField(verbose_name="Message", max_length=2000)
    phone = models.CharField(verbose_name="Phone number", max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.name + " " + self.email


class Feedback(models.Model):
    """Model for feedback"""
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
        return self.name

    @property
    def get_thumbnail_url(self):
        if self.thumbnail and hasattr(self.thumbnail, 'url'):
            return self.thumbnail .url
        else:
            return "/media/logos/default-thumb_dn1xzg.png"


class Image(models.Model):
    """Model for image files"""
    name = models.CharField(blank=True, null=True, max_length=250)
    url = models.URLField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="images")
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super(Image, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
        ordering = ["name"]

    def __str__(self):
        return self.name

    @property
    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/media/logos/default-thumb_dn1xzg.png"

