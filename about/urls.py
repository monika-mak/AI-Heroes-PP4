from . import views
from django import path

urlpatterns = [
    path('', views.about_me, name='about'),
]