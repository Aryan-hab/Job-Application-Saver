from django.contrib import admin
from django.urls import path, include
from applied_jobs import urls as jobs_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobs/', include(jobs_urls)),  # Include URLs from the `jobs` app
]
