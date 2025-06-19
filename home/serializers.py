from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Leadership, Profile, Contact, Feedback, Image, Video, Education, Skill, Portfolio, Course, MyContact, Experience


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class MyContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyContact
        fields = '__all__'

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'


class LeadershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leadership
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
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
            'user', 'title', 'biography','avatar', 'resume', 'work', 'all_experiences',
            'all_courses', 'all_leaderships', 'all_skills', 'all_projects', 'all_links', 'all_educations',
            'get_avatar_url', 'get_resume_url', 'get_work_samples_url'
        ]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['_debug'] = {
            'skills_count': instance.skills.count(),
            'courses_count': instance.courses.count(),
            'educations_count': instance.educations.count(),
            'id': instance.id
        }
        return rep


