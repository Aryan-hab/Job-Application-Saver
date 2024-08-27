from django import forms
from .models import Job


class JobListingForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['company_name', 'title', 'location', 'platform', 'application_date', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
