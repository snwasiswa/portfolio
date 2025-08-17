"""
serializers.py

Defines all Django REST Framework (DRF) serializers for the portfolio and resume application.

Serializers convert Django models to JSON (and vice versa) for API communication.
This includes models for user profiles, education, skills, experience, projects, media, and contact data.
"""

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    Leadership, Profile, Contact, Feedback, Image, Video,
    Education, Skill, Portfolio, Course, MyContact, Experience
)


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for Django's built-in User model.
    """
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class EducationSerializer(serializers.ModelSerializer):
    """
    Serializer for Education model.
    """
    class Meta:
        model = Education
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    """
    Serializer for Experience model.
    """
    class Meta:
        model = Experience
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    """
    Serializer for Skill model.
    """
    class Meta:
        model = Skill
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    """
    Serializer for Image model.
    """
    class Meta:
        model = Image
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    """
    Serializer for Video model.
    """
    class Meta:
        model = Video
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    """
    Serializer for Contact form submissions.
    """
    class Meta:
        model = Contact
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    """
    Serializer for Feedback model.
    """
    class Meta:
        model = Feedback
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    """
    Serializer for Course model.
    """
    class Meta:
        model = Course
        fields = '__all__'


class MyContactSerializer(serializers.ModelSerializer):
    """
    Serializer for custom contact information (e.g., links, social).
    """
    class Meta:
        model = MyContact
        fields = '__all__'


class PortfolioSerializer(serializers.ModelSerializer):
    """
    Serializer for Portfolio (project) model.
    """
    class Meta:
        model = Portfolio
        fields = '__all__'


class LeadershipSerializer(serializers.ModelSerializer):
    """
    Serializer for Leadership model.
    """
    class Meta:
        model = Leadership
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for Profile model, including nested related fields and media URLs.
    Adds a debug block in the representation output.
    """
    user = UserSerializer(read_only=True)
    all_experiences = ExperienceSerializer(many=True, read_only=True)
    all_courses = CourseSerializer(many=True, read_only=True)
    all_leaderships = LeadershipSerializer(many=True, read_only=True)
    all_skills = SkillSerializer(many=True, read_only=True)
    all_projects = PortfolioSerializer(many=True, read_only=True)
    all_links = MyContactSerializer(many=True, read_only=True)
    all_educations = EducationSerializer(many=True, read_only=True)
    get_avatar_url = serializers.ReadOnlyField()
    get_resume_url = serializers.ReadOnlyField()
    get_work_samples_url = serializers.ReadOnlyField()

    class Meta:
        model = Profile
        fields = [
            'user', 'title', 'biography', 'avatar', 'resume', 'work',
            'all_experiences', 'all_courses', 'all_leaderships', 'all_skills',
            'all_projects', 'all_links', 'all_educations',
            'get_avatar_url', 'get_resume_url', 'get_work_samples_url'
        ]

    def to_representation(self, instance):
        """
        Add custom debug information to the serialized output.

        Args:
            instance (Profile): The Profile instance being serialized.

        Returns:
            dict: The final representation with debug info appended.
        """
        rep = super().to_representation(instance)
        rep['_debug'] = {
            'skills_count': instance.skills.count(),
            'courses_count': instance.courses.count(),
            'educations_count': instance.educations.count(),
            'id': instance.id
        }
        return rep
