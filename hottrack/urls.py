from django.urls import path
from . import views

urlpatterns = [
    path(route="", view=views.index),
    path(route="<int:pk>/", view=views.song_detail),
]