from django.db import models
from cloudinary.models import CloudinaryField


class About(models.Model):
    """
    Represents the 'About' section of a website.
    """
    title = models.CharField(max_length=200)
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class CommunicationRequest(models.Model):
    """
    Represents a communication request submitted by a user.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    # Track if the request has been addressed
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Communication request from {self.name}"
