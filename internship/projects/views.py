from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Specialization
# Using mixins for class-based views
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.shortcuts import redirect, get_object_or_404
from django.views.generic.base import TemplateResponseMixin, View
from .forms import ModuleFormSet

# Adding content to specialization projects
from django.forms.models import modelform_factory
from django.apps import apps
from .models import Project, Content
from django.template import loader




# Create your views here.

# class-based views for the projects application
# class ManageSpecializationListView(ListView):
#  model = Specialization
#  template_name = 'projects/manage/specialization/list.html'

#  def get_queryset(self):
#     qs = super().get_queryset()
#     return qs.filter(owner=self.request.user)

class Project_LeadMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(project_lead=self.request.user)

class Project_LeadEditMixin:
    def form_valid(self, form):
        form.instance.project_lead = self.request.user
        return super().form_valid(form)

class Project_LeadSpecializationMixin(Project_LeadMixin, LoginRequiredMixin,PermissionRequiredMixin):
    model = Specialization
    fields = ['internship', 'title', 'slug', 'overview']
    success_url = reverse_lazy('manage_specialization_list')

class Project_LeadSpecializationEditMixin(Project_LeadSpecializationMixin, Project_LeadEditMixin):
    template_name = 'projects/manage/specialization/form.html'

class ManageSpecializationListView(Project_LeadSpecializationMixin, ListView):
    template_name = 'projects/manage/specialization/list.html'
    permission_required = 'projects.view_specialization'


class SpecializationCreateView(Project_LeadSpecializationEditMixin, CreateView):
    permission_required = 'projects.add_specialization'

class SpecializationUpdateView(Project_LeadSpecializationEditMixin, UpdateView):
    permission_required = 'projects.change_specialization'

class SpecializationDeleteView(Project_LeadSpecializationMixin, DeleteView):
    template_name = 'projects/manage/specialization/delete.html'
    permission_required = 'projects.delete_specialization'


class SpecializationProjectUpdateView(TemplateResponseMixin, View):
    template_name = 'projects/manage/project/formset.html'
    specialization = None
    def get_formset(self, data=None):
        return ModuleFormSet(instance=self.specialization, data=data)

    def dispatch(self, request, pk):
        self.specialization = get_object_or_404(Specialization, id=pk, project_lead=request.user)
        return super().dispatch(request, pk)
    
    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({'specialization': self.specialization,'formset': formset})
    
    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('manage_specialization_list')
        return self.render_to_response({
            'specialization': self.specialization,
            'formset': formset})

class ContentCreateUpdateView(TemplateResponseMixin, View):
    project = None
    model = None
    obj = None
    template_name = 'projects/manage/content/form.html'
    def get_model(self, model_name):
        if model_name in ['text', 'video', 'image', 'file']:
            return apps.get_model(app_label='projects', model_name=model_name)
 
        return None
    def get_form(self, model, *args, **kwargs):
        Form = modelform_factory(model, exclude=['project_lead', 'order', 'created','updated'])
        return Form(*args, **kwargs)
 
    def dispatch(self, request, project_id, model_name, id=None):
        self.project = get_object_or_404(Project, id=project_id, specialization__project_lead=request.user)
        self.model = self.get_model(model_name)
        if id:
            self.obj = get_object_or_404(self.model, id=id,project_lead=request.user)
        return super().dispatch(request, project_id, model_name, id)

    def get(self, request, project_id, model_name, id=None):
        form = self.get_form(self.model, instance=self.obj)
        return self.render_to_response({'form': form,'object': self.obj})

    def post(self, request, project_id, model_name, id=None):
        form = self.get_form(self.model,instance=self.obj, data=request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.project_lead = request.user
            obj.save()
            if not id:
                # new content
                Content.objects.create(project=self.project, item=obj)
            return redirect('project_content_list', self.project.id)
        return self.render_to_response({'form': form,'object': self.obj})

class ContentDeleteView(View):
    def post(self, request, id):
        content = get_object_or_404(Content, id=id, project__specialization__project_lead=request.user)
        project = content.project
        content.item.delete()
        content.delete()
        return redirect('project_content_list', project.id)

class ProjectContentListView(TemplateResponseMixin, View):
    # template = loader.get_template('signup.html')
    template_name = 'projects/manage/project/content_list.html'
    # template_name = loader.get_template('projects/manage/project/content_list.html')


    def get(self, request, project_id):
        project = get_object_or_404(Project, id=project_id, specialization__project_lead=request.user)
        return self.render_to_response({'project': project})