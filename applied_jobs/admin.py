from django.contrib import admin
from applied_jobs.models import Job


@admin.register(Job)
class JobsAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'title', 'location', 'application_date', 'status']
