from django.urls import path, re_path
from .converter import date
from . import views

urlpatterns = [
    path(route="", view=views.index),
    path(route="archives/<date:release_date>/", view=views.index),
    path(route="<int:pk>/cover.png", view=views.cover_png),
    path(route="export.csv", view=views.export_csv),
    re_path(
        route=r"^export\.(?P<format>(csv|xlsx))$", view=views.export, name="export"
    ),
]