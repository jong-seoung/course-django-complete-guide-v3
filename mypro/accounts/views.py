from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView as DjangoLoginView, RedirectURLMixin
from django.contrib.auth.views import LogoutView as DjangoLogoutView
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import LoginForm, SignupForm
from accounts.models import User
from accounts.utils import send_welcome_email


class SignupView(RedirectURLMixin, CreateView):
    model = User
    form_class = SignupForm
    template_name = "crispy_form.html"
    extra_context = {
        "form_title": "회원가입",
    }
    success_url = reverse_lazy("accounts:profile")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "회원가입을 환영합니다. ;-)")

        user = self.object
        auth_login(self.request, user)
        messages.success(self.request, "회원가입과 동시에 로그인 지원 !")
        send_welcome_email(user, fail_silently=True)

        return response


class LoginView(DjangoLoginView):
    form_class = LoginForm
    template_name = "crispy_form.html"
    extra_context = {
        "form_title": "로그인",
    }

class LogoutView(DjangoLogoutView):
    next_page = "accounts:login"

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.success(request, "로그아웃했습니다. :-)")
        return response


@login_required
def profile(request):
    return render(request, "accounts/profile.html")