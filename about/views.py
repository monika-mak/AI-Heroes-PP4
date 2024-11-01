from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CommunicationForm

# Create your views here.

def about_me(request, *args, **kwargs):
    """
    About page rendering
    """
    if request.method == "POST":
        communication_form = CommunicationForm(data=request.POST)
        if communication_form.is_valid():
            communication_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Collaboration request received! I endeavor to respond within 2 working days."
            )


    about = About.objects.all().order_by('-updated_on').first()
    communication_form = CommunicationForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
        "communication_form": communication_form,
        },
    )
