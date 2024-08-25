from django.urls import path
from django.views.generic import TemplateView

from .views import create_job_listing

urlpatterns = [
    path('create/', create_job_listing, name='create_job_listing'),
    path('success/', TemplateView.as_view(template_name='success.html'), name='success'),
]
