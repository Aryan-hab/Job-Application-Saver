from django.contrib import admin
from applied_jobs.models import Job


@admin.register(Job)
class JobsAdmin(admin.ModelAdmin):
    pass