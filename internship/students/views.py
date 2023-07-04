from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SpecializationEnrollForm
from django.views.generic.list import ListView
from projects.models import Specialization
from django.views.generic.detail import DetailView

class StudentRegistrationView(CreateView):
    template_name = 'students/student/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('student_specialization_list')
    def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'],
        password=cd['password1'])
        login(self.request, user)
        return result


class StudentEnrollSpecializationView(LoginRequiredMixin, FormView):
    specialization = None
    form_class = SpecializationEnrollForm
    def form_valid(self, form):
        self.specialization = form.cleaned_data['specialization']
        self.specialization.students.add(self.request.user)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('student_specialization_detail', args=[self.specialization.id])

class StudentSpecializationListView(LoginRequiredMixin, ListView):
    model = Specialization
    template_name = 'students/specialization/list.html'
    def get_queryset(self):
        qs =  super().get_queryset()
        return qs.filter(students__in=[self.request.user])

class StudentSpecializationDetailView(DetailView):
    model = Specialization
    template_name = 'students/specialization/detail.html'
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in=[self.request.user])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get specialization object
        specialization = self.get_object()
        if 'project_id' in self.kwargs:
            # get current project
            context['project'] = specialization.projects.get(id=self.kwargs['project_id'])
        else:
            # get first project
            context['project'] = specialization.projects.all()[0]
        return context