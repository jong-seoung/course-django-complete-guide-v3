from django.urls import path
from .views import index, NoteCreateView, NoteDetailView

app_name = "photolog"

urlpatterns = [
    path("", index, name="index"),
    path("new/", NoteCreateView.as_view(), name="note_new"),
    path("<int:pk>/", NoteDetailView.as_view(), name="note_detail"),
]
