from django import forms
from plan.models import Plan



class AddtoPlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['name']

