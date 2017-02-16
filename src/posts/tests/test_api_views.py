from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.utils import timezone

from rest_framework.test import APIRequestFactory, force_authenticate

from posts.api.views import (
		PostCreateAPIView,
		PostDetailAPIView,
		PostUpdateAPIView,
		PostDeleteAPIView,
		PostListAPIView,
	)

from posts.models import Post

User = get_user_model()

class PostAPITest(TestCase):
	def setUp(self):
		self.data = {"title": "some title", "content": "new content", "publish": timezone.now().date()}
		self.factory = APIRequestFactory()
		self.user = User.objects.create(
				username='test_username',
				email='test_email@gmail.com',
				password='test_password',
				is_staff=True,
				is_superuser=True,
			)

	def create_post(self, title="new title"):
		return Post.objects.create(title=title)

	def test_get_data(self):
		list_url = reverse("posts-api:list")
		obj = self.create_post()
		detail_url = reverse("posts-api:detail", kwargs={"slug": obj.slug})

		request = self.factory.get(list_url)
		response = PostListAPIView.as_view()(request)
		self.assertEqual(response.status_code, 200)

		request = self.factory.get(detail_url)
		response = PostDetailAPIView.as_view()(request, slug=obj.slug)
		self.assertEqual(response.status_code, 200)

	def test_post_data(self):
		create_url = reverse("posts-api:create")
		request = self.factory.post(create_url, data=self.data)
		response = PostCreateAPIView.as_view()(request)
		self.assertEqual(response.status_code, 401)
		force_authenticate(request, user=self.user)
		response = PostCreateAPIView.as_view()(request)
		self.assertEqual(response.status_code, 201)


	def test_update_data(self):
		obj = self.create_post()
		update_url = reverse("posts-api:update", kwargs={"slug": obj.slug})
		request = self.factory.put(update_url, data=self.data)
		response = PostUpdateAPIView.as_view()(request, slug=obj.slug)
		self.assertEqual(response.status_code, 401)
		force_authenticate(request, user=self.user)
		response = PostUpdateAPIView.as_view()(request, slug=obj.slug)
		self.assertEqual(response.status_code, 200)

	def test_delete_data(self):
		obj = self.create_post()
		delete_url = reverse("posts-api:delete", kwargs={"slug": obj.slug})
		request = self.factory.delete(delete_url, data=self.data)
		response = PostDeleteAPIView.as_view()(request, slug=obj.slug)
		self.assertEqual(response.status_code, 401)
		force_authenticate(request, user=self.user)
		response = PostDeleteAPIView.as_view()(request, slug=obj.slug)
		self.assertEqual(response.status_code, 204)










