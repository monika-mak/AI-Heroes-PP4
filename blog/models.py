from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models import Count

STATUS = ((0, "Draft"), (1, "Published"))
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts'
)
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on=models.DateTimeField(auto_now=True)


    class Meta:  # additional information about the model/order of the post (descending if - at the front)
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"

    # count votes for each post
    def vote_count(self):
        return self.post_votes.count()


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='commenter')
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:  # dditional information about the model/order of the post (descending if '-' at the front)
        ordering = ['created_on']

    def __str__(self):  # displays posts title
        return f"Comment: {self.body} by {self.author}"


#https://www.geeksforgeeks.org/how-to-filter-foreignkey-choices-in-a-django-modelform/

class Vote(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='post_votes')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_votes')
    created_on = models.DateTimeField(auto_now_add=True)

    # https://www.geeksforgeeks.org/how-to-define-two-fields-unique-as-couple-in-django/
    # ensure one user can vote only once on the particular vote
    class Meta:
        unique_together = ('post', 'author')
        

