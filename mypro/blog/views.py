from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django_nextjs.render import render_nextjs_page

from blog.models import Post


@cache_page(600)
def index(request):
    post_qs = Post.objects.all()
    return render(
        request,
        "blog/index.html",
        {
            "post_list": post_qs,
        },
    )


def whoami(request):
    status = 200 if request.user.is_authenticated else 401
    username = request.user.username or "anonymous"
    return HttpResponse(f"Your username is <strong>{username}</strong>.", status=status)
