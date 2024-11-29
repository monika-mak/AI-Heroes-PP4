from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CommunicationForm


def about_me(request, *args, **kwargs):
    """
    Renders the About page with optional form to submit collaboration requests.
    """
    if request.method == "POST":
        # Handle form submission
        communication_form = CommunicationForm(data=request.POST)
        if communication_form.is_valid():
            # Save the form data and display a success message
            communication_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Collaboration request received!"
            )
        else:
            messages.add_message(
                request, messages.ERROR,
                "Validation Error. Please check email format."
                )

    # Save the form data and display a success message
    about = About.objects.all().order_by('-updated_on').first()
    # Initialize an empty CommunicationForm for display
    communication_form = CommunicationForm()
    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "communication_form": communication_form,
        },
    )
