from django import forms
from django.forms.models import inlineformset_factory
from .models import Specialization, Project

ModuleFormSet = inlineformset_factory(Specialization, Project, 
fields=['title', 'description', 'order'], extra=1, can_delete=True)