"""
views.py

This file defines the web and API views for a personal portfolio and resume web application.
It includes:

- Template views for rendering pages like home, about, resume, contact, and projects.
- API endpoints using Django REST Framework (DRF) for managing and accessing data such as
  education, skills, experience, portfolio, profile, etc.
- PDF generation view to create and serve resume content securely as a downloadable file.

Technologies used:
- Django for web page rendering.
- Django REST Framework for API serialization and viewsets.
- WeasyPrint for generating PDF files.
"""

from django.shortcuts import render
from django.views import generic
from home.forms import ContactForm
from .models import (
    Leadership, Portfolio, Skill, Education, Course, MyContact,
    Feedback, Image, Contact, Video, Profile, Experience
)
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from rest_framework import viewsets
from .serializers import (
    EducationSerializer, ContactSerializer, PortfolioSerializer, SkillSerializer,
    ImageSerializer, ProfileSerializer, MyContactSerializer, FeedbackSerializer,
    CourseSerializer, LeadershipSerializer, VideoSerializer, ExperienceSerializer
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse, FileResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import tempfile


# ------------------ Django Template Views ------------------ #

def home(request):
    """
    Renders the homepage of the website.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered homepage HTML.
    """
    return render(request, 'home.html')


class AboutView(generic.TemplateView):
    """
    Displays the 'About' page with active contact information.
    """
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        """
        Adds active contacts to the context.

        Args:
            **kwargs: Additional context arguments.

        Returns:
            dict: Context data with active contacts.
        """
        context = super().get_context_data(**kwargs)
        contacts = MyContact.objects.filter(is_active=True)
        context["contacts"] = contacts
        return context


class ResumeView(generic.TemplateView):
    """
    Displays the main resume page with educational background.
    """
    template_name = "resume.html"

    def get_context_data(self, **kwargs):
        """
        Adds active education records to the context.

        Args:
            **kwargs: Additional context arguments.

        Returns:
            dict: Context data including education information.
        """
        context = super().get_context_data(**kwargs)
        educations = Education.objects.filter(is_active=True)
        context["educations"] = educations
        return context


class ResumeCoursesView(generic.TemplateView):
    """
    Displays a list of courses completed or in progress.
    """
    template_name = "courses.html"

    def get_context_data(self, **kwargs):
        """
        Adds active courses to the context.

        Args:
            **kwargs: Additional context arguments.

        Returns:
            dict: Context data including course records.
        """
        context = super().get_context_data(**kwargs)
        courses = Course.objects.filter(is_active=True)
        context["courses"] = courses
        return context


class ResumeProjectsView(generic.TemplateView):
    """
    Displays a list of portfolio projects as part of the resume.
    """
    template_name = "resumeprojects.html"

    def get_context_data(self, **kwargs):
        """
        Adds active portfolio projects to the context.

        Args:
            **kwargs: Additional context arguments.

        Returns:
            dict: Context data including projects.
        """
        context = super().get_context_data(**kwargs)
        projects = Portfolio.objects.filter(is_active=True)
        context["projects"] = projects
        return context


class ResumeLeadershipView(generic.TemplateView):
    """
    Displays leadership and involvement records.
    """
    template_name = "leadership.html"

    def get_context_data(self, **kwargs):
        """
        Adds active leadership records to the context.

        Args:
            **kwargs: Additional context arguments.

        Returns:
            dict: Context data including leadership entries.
        """
        context = super().get_context_data(**kwargs)
        leaderships = Leadership.objects.filter(is_active=True)
        context["leaderships"] = leaderships
        return context


class ResumeSkillsView(generic.TemplateView):
    """
    Displays a list of personal and professional skills.
    """
    template_name = "skills.html"

    def get_context_data(self, **kwargs):
        """
        Adds active skills to the context.

        Args:
            **kwargs: Additional context arguments.

        Returns:
            dict: Context data including skill entries.
        """
        context = super().get_context_data(**kwargs)
        skills = Skill.objects.filter(is_active=True)
        context["skills"] = skills
        return context


class PortfolioView(generic.ListView):
    """
    Displays a paginated list of portfolio projects.
    """
    template_name = "projects.html"
    model = Portfolio
    context_object_name = 'projects'
    paginate_by = 6

    def get_queryset(self):
        """
        Retrieves only active portfolio projects.

        Returns:
            QuerySet: Filtered queryset of active projects.
        """
        return super().get_queryset().filter(is_active=True)


class PortfolioDetailView(generic.DetailView):
    """
    Displays details for a single portfolio project.
    """
    model = Portfolio
    template_name = "portfolio_details.html"


class ContactView(generic.FormView, SuccessMessageMixin):
    """
    Renders the contact form and handles user messages.
    """
    template_name = "contact.html"
    form_class = ContactForm
    success_url = 'contact'

    def get_context_data(self, **kwargs):
        """
        Adds active contact information to the context.

        Args:
            **kwargs: Additional context arguments.

        Returns:
            dict: Context data with contact methods.
        """
        context = super().get_context_data(**kwargs)
        contacts = MyContact.objects.filter(is_active=True)
        context["contacts"] = contacts
        return context

    def form_valid(self, form):
        """
        Processes and saves the contact form submission.

        Args:
            form (ContactForm): Validated form instance.

        Returns:
            HttpResponseRedirect: Redirects to success URL with a message.
        """
        form.send_email()
        form.save()
        messages.success(self.request, 'Your message has been submitted. Thank you!')
        return super().form_valid(form)


# ------------------ DRF API ViewSets ------------------ #

class EducationViewSet(viewsets.ModelViewSet):
    """
    API endpoint to perform CRUD operations on Education objects.
    """
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class ExperienceViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing professional experience data.
    """
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class LeadershipViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing leadership and extracurricular involvement records.
    """
    queryset = Leadership.objects.all()
    serializer_class = LeadershipSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing completed or ongoing courses.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing uploaded images.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class VideoViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing videos (e.g., presentations, demo reels).
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class MyContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint for dynamic contact entries used throughout the site.
    """
    queryset = MyContact.objects.all()
    serializer_class = MyContactSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    """
    API endpoint for capturing and retrieving visitor feedback.
    """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class SkillViewSet(viewsets.ModelViewSet):
    """
    API endpoint for listing and managing skills.
    """
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing profile data and associated records.
    Prefetches related models for performance optimization.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        """
        Optimizes data fetching by preloading related models.

        Returns:
            QuerySet: Prefetched Profile queryset.
        """
        return Profile.objects.prefetch_related(
            'skills',
            'courses',
            'educations',
            'links',
            'leaderships',
            'projects'
        )


class PortfolioViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing portfolio projects.
    """
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing contact form entries.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


# ------------------ PDF Resume View ------------------ #

@method_decorator(csrf_exempt, name='dispatch')
class ResumePDFView(APIView):
    """
    API endpoint that retrieves an uploaded resume PDF file after verifying a password.

    Methods:
        post(request): Validates password and returns the uploaded resume PDF.

    Attributes:
        permission_classes (list): Allows access to all users.
    """
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        """
        Handles POST request to verify password and return uploaded resume PDF.

        Args:
            request (Request): The HTTP request object with 'password' in body.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: PDF file as HTTP response or error if password invalid or file inaccessible.
        """
        # Extract password from request data
        password = request.data.get('password')

        # Retrieve the first Profile instance (replace as needed)
        profile = Profile.objects.first()

        # Return 404 if no profile found
        if not profile:
            return Response({'error': 'Profile not found'}, status=404)

        # Validate password against hashed resume_password field
        if not password or not check_password(password, profile.resume_password):
            return Response({'error': 'Incorrect password'}, status=403)

        # Check if resume file is uploaded
        if not profile.resume:
            return Response({'error': 'Resume file not uploaded'}, status=404)

        try:
            # Attempt to open the resume file
            file_field = profile.resume

            # Open file in binary read mode and return as downloadable response
            response = FileResponse(
                file_field.open('rb'),
                as_attachment=True,
                filename='resume.pdf',
                content_type='application/pdf'
            )
            return response

        except Exception as e:
            return Response({'error': f'Failed to read resume file: {str(e)}'}, status=500)
