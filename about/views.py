from django.shortcuts import render
from .models import About
from .forms import CommunicationForm

# Create your views here.

def about_me(request, *args, **kwargs):
    """
    About page rendering
    """
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
