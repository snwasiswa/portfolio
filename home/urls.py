"""
urls.py

Defines the URL routes for the personal portfolio and resume web application.

This includes:
- Public website pages (home, about, resume, contact, portfolio, etc.)
- PDF resume generation endpoint
- Custom admin branding
"""

from django.contrib import admin
from django.urls import path, include
from home import views
from .views import ResumePDFView

# ----------------- Django Admin Customization ----------------- #
admin.site.site_header = "Steve Wasiswa"
admin.site.site_title = "Welcome to Steve's Dashboard"
admin.site.index_title = "Welcome to the Portal"

# ----------------- URL Patterns ----------------- #
urlpatterns = [
    # Home Page
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),

    # Static Pages
    path('about', views.AboutView.as_view(), name='about'),
    path('contact', views.ContactView.as_view(), name='contact'),

    # Resume Pages
    path('resume', views.ResumeView.as_view(), name='resume'),
    path('education', views.ResumeView.as_view(), name='education'),  # Alias for resume
    path('skills', views.ResumeSkillsView.as_view(), name='skills'),
    path('courses', views.ResumeCoursesView.as_view(), name='courses'),
    path('resumeprojects', views.ResumeProjectsView.as_view(), name='resumeprojects'),
    path('leadership', views.ResumeLeadershipView.as_view(), name='leadership'),

    # Portfolio Pages
    path('portfolio/', views.PortfolioView.as_view(), name='portfolio'),
    path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name='portfolio_details'),

    # API Endpoint for PDF Resume Download
    path('api/download-resume/', ResumePDFView.as_view(), name='download_resume'),
]
