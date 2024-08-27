from django.db import models
from cities_light.models import City


statuses = [
    ('PE', 'Pending'),
    ('INT', 'Interview Invitation'),
    ('RE', 'Rejected'),
    ('WI', 'Withdrawn by candidate')
]


class Job(models.Model):
    company_name = models.CharField(max_length=30, null=False, blank=False)
    title = models.CharField(max_length=30, null=False, blank=False)
    location = models.ForeignKey(City, on_delete=models.PROTECT, null=True, blank=True)
    platform = models.CharField(max_length=30, null=True, blank=False)
    application_date = models.DateTimeField(auto_now_add=False)
    status = models.CharField(max_length=30, null=False, blank=False, choices=statuses, default='PE')
    description = models.TextField(blank=False, null=False)

    def __str__(self):
        return f"{self.company_name}"

