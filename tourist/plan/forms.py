from django import forms
from plan.models import Plan

class CreatePlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['name', 'detail']
