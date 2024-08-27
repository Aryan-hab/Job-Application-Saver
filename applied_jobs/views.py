from django.shortcuts import render
from .forms import JobListingForm


def create_job_listing(request):
    success_message = None  # Initialize success_message
    if request.method == 'POST':
        form = JobListingForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "Job listing created successfully!"
            form = JobListingForm()  # Reset the form after successful submission
    else:
        form = JobListingForm()

    return render(request, 'create_job_listing.html', {'form': form, 'success_message': success_message})
