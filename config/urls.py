from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(route="hottrack/", view=include("hottrack.urls")),
    path(route="", view=lambda request: redircet("hottrack/")),
]

if settings.DEBUG:
    urlpatterns += [
        path(route="__debug__/", view=include("debug_toolbar.urls")),
    ]
    