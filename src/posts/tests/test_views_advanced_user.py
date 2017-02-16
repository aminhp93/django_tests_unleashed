from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory
from django.utils.text import slugify

from posts.models import Post
from posts.views import post_update, post_create
# Create your tests here.

User = get_user_model()

class PostViewAdvancedTestCase(TestCase):
	def setUp(self):
		self.factory = RequestFactory()
		self.user = User.objects.create(
				username='test_username',
				email='test_email@gmail.com',
				password='test_password',
				is_staff=True,
				is_superuser=True,
			)

	def create_post(self, title="This title"):
		return Post.objects.create(title=title)

	def test_user_auth(self):
		obj = self.create_post(title="Test title")
		edit_url = reverse("posts:update", kwargs={'slug': obj.slug})
		request = self.factory.get(edit_url)
		request.user = self.user

		response = post_update(request, slug=obj.slug)

		self.assertEqual(response.status_code, 200)

	def test_user_post(self):
		obj = self.create_post(title="Test title")
		request = self.factory.post("/posts/create")
		request.user = self.user

		response = post_create(request)

		self.assertEqual(response.status_code, 200)

	# def test_list_view(self):
	# 	list_url = reverse("posts:list")
	# 	response = self.client.get(list_url)
	# 	self.assertEqual(response.status_code, 200)

	# def test_detail_view(self):
	# 	obj = self.create_post(title="Another new title")
	# 	response = self.client.get(obj.get_absolute_url())
	# 	self.assertEqual(response.status_code, 200)

	# def test_update_view(self):
	# 	obj = self.create_post(title="Another new title")
	# 	edit_url = reverse("posts:update", kwargs={"slug": obj.slug})
	# 	print(edit_url)

	# 	response = self.client.get(edit_url)
	# 	print(response)
	# 	self.assertEqual(response.status_code, 404)

	# def test_delete_view(self):
	# 	obj = self.create_post(title="Another new title")
	# 	delete_url = reverse("posts:delete", kwargs={"slug": obj.slug})
	# 	print(delete_url)

	# 	response = self.client.get(delete_url)
	# 	print(response)
	# 	self.assertEqual(response.status_code, 404)