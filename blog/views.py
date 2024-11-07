from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment, Vote
from .forms import CommentForm
from django.db.models import Count
from django.contrib.auth.decorators import login_required

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
    post = ( 
        Post.objects.filter(status=1)
        .annotate(vote_count=Count('post_votes'))
        .order_by('-vote_count') # [:5]
        )
    return render(request, 'blog/leaderboard.html', {'posts': post})


@login_required 
def vote_on_a_post(request, post):
    '''
    view to handle all the votes given to individual posts
    no one post can recieve more than one vote from the same user
    '''
    post = get_object_or_404(Post, id=pk)

    create instance for user to vote on a blog
    # Check if user already voted for this post
    if user exists and they click on a post 
        the post is noted
    elif they dont exist they have to login to vote
        message "you need to log in"
    else the vote is deleted and they can vote again
    


    if not Vote.objects.filter(post=post, author=request.user).exists():
        Vote.objects.create(post=post, author=request.user)
        messages.success(request, "Thank you for your vote")
    else:
        messages.info(request, "You have already voted for this Hero")
    return redirect(reverse('home'))

    def already_voted(user):
        if user.vote ==True:
            messages.info(request, "You have already voted")

