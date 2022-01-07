from django.shortcuts import render, HttpResponse
from django.template.defaultfilters import truncatechars_html
from django.views import generic

from home.forms import ContactForm
from .models import Leadership, Portfolio, Profile, Skill, Education, Feedback, Image, Contact, Course
from django.contrib import messages

from django.views.generic.list import ListView
from django.views.generic.base import TemplateResponseMixin, View, TemplateView


# Create your views here.

def home(request):
    # return HttpResponse("This is my homepage(/)")
    return render(request,'home.html')


def about(request):
    # return HttpResponse("This is my about(/)")
    return render(request,'about.html')

def covid_19(request):
     #return HttpResponse("This is coronavirus update page")
    return render(request,'covid_19.html') 

def summarizer(request):
     #return HttpResponse("This is summarizer(/) app page")
    return render(request,'summarizer.html')

def summarizerapp(request):
     #return HttpResponse("This is summarizer(/) app page")
    return render(request,'summarizerapp.html')

def projects(request):
     #return HttpResponse("This is summarizer(/) app page")
    return render(request,'projects.html')



def leadership(request):

    return render(request,'leadership.html')

def resumeprojects(request):

    return render(request,'resumeprojects.html')


   
class ResumeView(generic.TemplateView):
    """View for the first page of the resume"""
    template_name = "resume.html"

    def get_context_data(self, **kwargs):
        
        context =  super().get_context_data(**kwargs)
        educations = Education.objects.filter(is_active=True)  
        context["educations"] = educations
    
        return context

class ResumeCoursesView(generic.TemplateView):
    """View for the courses of the resume"""
    template_name = "courses.html"

    def get_context_data(self, **kwargs):
        
        context =  super().get_context_data(**kwargs)
        courses = Course.objects.filter(is_active=True)        
        context["courses"] = courses

        return context

class ResumeProjectsView(generic.TemplateView):
    """View for the projects of the resume"""
    template_name = "resumeprojects.html"

    def get_context_data(self, **kwargs):
        
        context =  super().get_context_data(**kwargs)
        projects = Portfolio.objects.filter(is_active=True)        
        context["projects"] = projects

        return context

class ResumeLeadershipView(generic.TemplateView):
    """View for the campus involvement"""
    template_name = "leadership.html"

    def get_context_data(self, **kwargs):
        
        context =  super().get_context_data(**kwargs)
        leaderships = Leadership.objects.filter(is_active=True)        
        context["leaderships"] = leaderships

        return context


class ResumeSkillsView(generic.TemplateView):
    """View for the skills"""
    template_name = "skills.html"

    def get_context_data(self, **kwargs):
        
        context =  super().get_context_data(**kwargs)
        skills = Skill.objects.filter(is_active=True)        
        context["skills"] = skills

        return context

class PortfolioView(generic.ListView):
    """View for portfolio"""
    template_name = "projects.html"
    model = Portfolio
    context_object_name = 'projects'
    paginate_by = 6
    

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class PortfolioDetailView(generic.DetailView):
    """View for portfolio details"""
    model = Portfolio
    template_name = "portfolio_details.html"


class ContactView(generic.FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your message has been submitted. Thank you!')
        return super().form_valid(form)
