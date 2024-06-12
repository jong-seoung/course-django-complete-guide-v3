from django.urls import path
from . import views

urlpatterns = [
    path(route="", view=views.index),
    path(route="<int:pk>/", view=views.song_detail),
    path(route="melon-<int:melon_uid>/", view=views.song_detail),
    path(
        route="archives/<int:year>/",
        view=views.SongYearArchiveView.as_view(),
        name="song_archive_year",
    ),
    path(
        route="archives/<int:year>/<int:month>/",
        view=views.SongMonthArchiveView.as_view(),
        name="song_archive_month",
    ),
    path(
        route="archives/<int:year>/<int:month>/<int:day>/",
        view=views.SongDayArchiveView.as_view(),
        name="song_archive_day",
    ),
    path(
        route="archives/today/",
        view=views.SongTodayArchiveView.as_view(),
        name="song_archive_today",
    ),
]