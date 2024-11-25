from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models import Count

# Status choices for posts
STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Represents a blog post with title, author, content, status, and metadata.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts'
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)  # allow for empty values

    class Meta:  # Orders posts by creation date, descending
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"

    # count votes for each post
    def vote_count(self):
        """
        Returns the number of votes a post has received.
        """
        return self.post_votes.count()


class Comment(models.Model):
    """
    Represents a comment on a blog post.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='commenter')
    body = models.TextField()
    approved = models.BooleanField(default=False)  # Requires admin approval
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']  # Orders comments by creation date

    def __str__(self):  # displays posts title
        return f"Comment: {self.body} by {self.author}"


# https://www.geeksforgeeks.org
# /how-to-filter-foreignkey-choices-in-a-django-modelform/
class Vote(models.Model):
    """
    Represents a user's vote on a blog post.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='post_votes')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_votes')
    created_on = models.DateTimeField(auto_now_add=True)

    # https://www.geeksforgeeks.org/how-to-define-two-fields-unique-as-couple-in-django/
    # ensure each user can vote on a post only once
    class Meta:
        unique_together = ('post', 'author')
