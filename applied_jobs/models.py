from django.db import models


class Job(models.Model):
    company_name = models.CharField(max_length=30, null=False, blank=False)
    title = models.CharField(max_length=30, null=False, blank=False)
    location = models.CharField(max_length=30, null=True, blank=True)
    application_date = models.DateTimeField(auto_now_add=False)
    description = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.company_name

