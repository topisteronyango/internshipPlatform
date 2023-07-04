from django import forms
from projects.models import Specialization
class SpecializationEnrollForm(forms.Form):
    specialization = forms.ModelChoiceField(queryset=Specialization.objects.all(), widget=forms.HiddenInput)