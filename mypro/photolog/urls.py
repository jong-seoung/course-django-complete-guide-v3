from django.urls import path
from .views import index, note_edit, NoteCreateView, NoteDetailView, CommentCreateView, CommentListView, CommentUpdateView, CommentDeleteView, user_page, user_follow

app_name = "photolog"

urlpatterns = [
    path("", index, name="index"),
    path("new/", NoteCreateView.as_view(), name="note_new"),
    path("@<username>/", user_page, name="user_page"),
    path(
        "@<username>/follow/",
        user_follow,
        name="user_follow",
        kwargs={"action": "follow"},
    ),
    path(
        "@<username>/unfollow/",
        user_follow,
        name="user_unfollow",
        kwargs={"action": "unfollow"},
    ),
    path("<int:pk>/", NoteDetailView.as_view(), name="note_detail"),
    path("<int:pk>/edit/", note_edit, name="note_edit"),
    path("<int:note_pk>/comments/", CommentListView.as_view(), name="comment_list"),
    path("<int:note_pk>/comments/new/", CommentCreateView.as_view(), name="comment_new"),
    path(
        "<int:note_pk>/comments/<int:pk>/edit/", CommentUpdateView.as_view(), name="comment_edit"
    ),
        path(
        "<int:note_pk>/comments/<int:pk>/delete/",
        CommentDeleteView.as_view(),
        name="comment_delete",
    ),
]
