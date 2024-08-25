from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from applied_jobs import urls as jobs_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobs/', include(jobs_urls)),  # Include URLs from the `jobs` app
    path('', RedirectView.as_view(url='/jobs/create/', permanent=False)),  # Redirect root to jobs/create

]
