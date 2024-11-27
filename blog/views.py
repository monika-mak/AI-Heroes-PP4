from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment, Vote
from .forms import CommentForm
from django.db.models import Count, Q, Value, BooleanField
# from django.shortcuts import render


# def custom_404_view(request, exception):
#     return render(request, 'errors/404.html', status=404)

# def custom_500_view(request):
#     return render(request, 'errors/500.html', status=500)

# def custom_403_view(request, exception):
#     return render(request, 'errors/403.html', status=403)

# def custom_400_view(request, exception):
#     return render(request, 'errors/400.html', status=400)

# from django.core.exceptions import PermissionDenied

# def some_view(request):
#     raise PermissionDenied

    
class PostList(generic.ListView):
    """
    View to display a paginated list of published posts.
    Annotates each post with the number of comments
    and whether the user has voted on it.
    """
    queryset = Post.objects.filter(status=1).annotate(comment_count=Count(
        'comments'))
    template_name = "blog/index.html"
    paginate_by = 6

    def get_queryset(self):
        """
        Customizes the queryset to include vote annotations
        for authenticated users.
        """
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            # Annotate whether the user has voted on the post
            queryset = queryset.annotate(
                voted=Count('post_votes', filter=Q(
                    post_votes__author=self.request.user))
            )
        else:
            # Add a default value for non-authenticated users
            queryset = queryset.annotate(
                voted=Value(False, output_field=BooleanField()))
        return queryset


def post_detail(request, slug):
    """
    Displays an individual post along with its comments.
    Handles comment form submission and checks
    whether the user has voted on the post.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    # check if user has already voted on a post
    voted = False
    if request.user.is_authenticated:
        voted = Vote.objects.filter(post=post, author=request.user).exists()

    # handle comment form submission
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "voted": voted,
        },
    )


def comment_edit(request, slug, comment_id):
    """
    Allows users to edit their comments on a specific post.
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating comment!'
                )

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Allows users to delete their comments on a specific post.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!'
            )

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# Leaderboard view to display posts ordered by the number of votes
def leaderboard(request):
    """
    Displays the top 5 posts ranked by the number of votes.
    """
    posts = (
        Post.objects.filter(status=1)
        .annotate(vote_count=Count('post_votes'))
        .order_by('-vote_count')[:5]  # only top 5 positions are displayed
        )
    return render(request, 'blog/leaderboard.html', {'posts': posts})


def vote_on_a_post(request, post_id):
    """
    Allows authenticated users to vote on a post.
    A user can vote on up to 3 posts
    and cannot vote multiple times on the same post.
    """

    post = get_object_or_404(Post, id=post_id)
    voted = False
    if request.user.is_authenticated:
        voted = Vote.objects.filter(post=post, author=request.user).exists()

    if not request.user.is_authenticated:
        # Redirect unauthenticated users to the login page
        messages.info(request, "You need to log in to cast a vote")
        return redirect('account_login')

    if Vote.objects.filter(post=post, author=request.user).exists():
        # Remove vote if the user has already voted
        Vote.objects.filter(post=post, author=request.user).delete()
        messages.info(request, 'Vote cancelled')
    else:
        # Inform user if a maximum of 3 votes limit was reached
        if request.user.user_votes.count() >= 3:
            messages.info(request, "You've reached the maximum votes limit")
        else:
            # create vote if user is eligible
            Vote.objects.create(post=post, author=request.user)
            messages.success(request, "Thank you for your vote")
    # Redirect back to the referring page
    # https://docs.djangoproject.com/en/5.1/ref/request-response/#django.http.HttpRequest.META
    referrer = request.META.get('HTTP_REFERER', '/')
    return HttpResponseRedirect(referrer)
