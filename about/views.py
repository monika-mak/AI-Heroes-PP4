from django.shortcuts import render
from .models import About
# Create your views here.

def about_me(request, *args, **kwargs):
    """
    About page rendering
    """
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )
