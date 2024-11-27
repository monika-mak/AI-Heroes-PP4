from . import views
from django.urls import path
from .views import leaderboard
from .views import vote_on_a_post


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('vote/<int:post_id>/', views.vote_on_a_post, name='vote_on_a_post'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path(
        '<slug:slug>/edit_comment/<int:comment_id>',
        views.comment_edit, name='comment_edit'
        ),
    path(
        '<slug:slug>/delete_comment/<int:comment_id>',
        views.comment_delete, name='comment_delete'
        ),
]
