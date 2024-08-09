# blog/tests/test_api.py

import base64

import pytest
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APIClient

from accounts.models import User
from accounts.tests.factories import UserFactory
from blog.models import Post
from blog.tests.factories import PostFactory


def create_user(raw_password: str = None) -> User:
    """새로운 User 레코드를 생성 및 반환"""
    return UserFactory(raw_password=raw_password)


def get_api_client_with_basic_auth(user: User, raw_password: str) -> APIClient:
    """인자의 User 인스턴스와 암호 기반에서 Basic 인증을 적용한 APIClient 인스턴스 반환"""

    # *.http 파일에서는 자동으로 base64 인코딩을 수행해줬었습니다.
    base64_data: bytes = f"{user.username}:{raw_password}".encode()
    authorization_header: str = base64.b64encode(base64_data).decode()

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Basic {authorization_header}")
    return client


@pytest.fixture
def unauthenticated_api_client() -> APIClient:
    """Authorization 인증 헤더가 없는 기본 APIClient 인스턴스 반환"""
    return APIClient()


@pytest.fixture
def api_client_with_new_user_basic_auth(faker) -> APIClient:
    """새로운 User 레코드를 생성하고, 그 User의 인증 정보가 Authorization 헤더로 지정된 APIClient 인스턴스 반환"""
    raw_password: str = faker.password()
    user: User = create_user(raw_password)
    api_client: APIClient = get_api_client_with_basic_auth(user, raw_password)
    return api_client


@pytest.fixture
def new_user() -> User:
    """새로운 User 레코드를 생성 및 반환"""
    return create_user()


@pytest.fixture
def new_post() -> Post:
    """새로운 Post 레코드를 반환"""
    return PostFactory()


@pytest.mark.it(
    "게시물 목록 조회. 비인증 조회가 가능해야하며, 생성한 포스팅의 개수만큼 응답을 받아야 합니다."
)
@pytest.mark.django_db
def test_post_list(unauthenticated_api_client):
    post_list = [PostFactory() for __ in range(10)]

    url = reverse("api-v1:post_list")
    response: Response = unauthenticated_api_client.get(url)
    assert status.HTTP_200_OK == response.status_code
    assert len(post_list) == len(response.data["result"])


@pytest.mark.it(
    "특정 게시물 조회. 비인증 조회가 가능해야하며, 생성한 포스팅을 조회할 수 있어야 합니다."
)
@pytest.mark.django_db
def test_post_retrieve(unauthenticated_api_client):
    new_post = PostFactory()

    url: str = reverse("api-v1:post_detail", args=[new_post.pk])
    response: Response = unauthenticated_api_client.get(url)
    assert status.HTTP_200_OK == response.status_code
    assert new_post.title == response.data["result"]["title"]