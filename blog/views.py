from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment, Vote
from .forms import CommentForm
from django.db.models import Count

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).annotate(comment_count=Count('comments'))
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
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
            "comment_form": comment_form
        },
    )

def comment_edit(request, slug, comment_id):
    """
    view to edit comments
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
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))   


# Leaderboard view to display posts ordered by the number of votes     
def leaderboard(request):
    posts = ( 
        Post.objects.filter(status=1)
        .annotate(vote_count=Count('post_votes'))
        .order_by('-vote_count')[:5] # ensure only top 5 positions are displayed
        )
    return render(request, 'blog/leaderboard.html', {'posts': posts})


def vote_on_a_post(request, post_id):
    '''
    view to handle all the votes given to individual posts
    no one post can recieve more than one vote from the same user
    '''

    post = get_object_or_404(Post, id=post_id)
    
    # Check if user is logged in 
    if not request.user.is_authenticated:
        messages.info(request, "You need to log in to cast a vote")
        return redirect('login')
    # if user already voted on this blog, remove vote
    if Vote.objects.filter(post=post, author=request.user).exists():
        Vote.objects.filter(post=post, author=request.user).delete()
        messages.info(request, 'Unvoted, change colors of vote icon')
        return redirect('leaderboard')
    else:
        # get the total amount of votes per user and check if not exceeding 3
        if request.user.user_votes.count() >= 3:
            messages.info(request, "You 've reached max 3 votes limit ")
            return redirect('leaderboard')
        else:
            # create vote if no previous restrictions are valid
            Vote.objects.create(post=post, author=request.user)
            messages.success(request, "Thank you for your vote")
            return redirect('leaderboard')





 
