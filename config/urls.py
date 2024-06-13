from django.conf import settings
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.views.generic import RedirectView, TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path(route="core/", view=include("core.urls")),
    path(route="hottrack/", view=include("hottrack.urls")),
    path("", RedirectView.as_view(pattern_name="hottrack:index")),
    ]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
    