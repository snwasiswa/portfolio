from django.contrib import admin
from django.urls import path, include
from home import views

# Customization of django admin
admin.site.site_header = "Steve Wasiswa"
admin.site.site_title = "Welcome to Steve's Dashboard"
admin.site.index_title = "Welcome to the Portal"

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('portfolio/', views.PortfolioView.as_view(), name='portfolio'),
    path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name='portfolio_details'),
    path('about', views.about, name='about'),
    path('resume', views.ResumeView.as_view(), name='resume'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('summarizer', views.summarizer, name='summarizer'),
    path('covid_19', views.covid_19, name='covid_19'),
    path('summarizerapp', views.summarizerapp, name='summarizerapp'),
    path('resumeprojects', views.ResumeProjectsView.as_view(), name='resumeprojects'),
    path('skills', views.ResumeSkillsView.as_view(), name='skills'),
    path('courses', views.ResumeCoursesView.as_view(), name='courses'),
    path('education', views.ResumeView.as_view(), name='education'),
    path('leadership', views.ResumeLeadershipView.as_view(), name='leadership'),

]
