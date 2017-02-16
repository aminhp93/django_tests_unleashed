from django.test import TestCase
from django.utils.text import slugify
from django.utils import timezone

from posts.forms import PostForm
from posts.models import Post
# Create your tests here.

class PostFormTestCase(TestCase):

	def test_valid_form(self):
		title = "A new title"
		slug = "slug-is-unique"
		content = "some content"
		obj = Post.objects.create(title=title, slug=slug, publish=timezone.now(), content=content)
		data = {'title': obj.title, "slug": obj.slug, "publish": obj.publish, "content": content}
		form = PostForm(data=data)
		self.assertTrue(form.is_valid())
		self.assertEqual(form.cleaned_data.get('title'), obj.title)
		self.assertNotEqual(form.cleaned_data.get('content'), "test")

	def test_invalid_form(self):
		title = "A new title"
		slug = "slug-is-unique"
		content = "some content"
		obj = Post.objects.create(title=title, slug=slug, publish=timezone.now(), content=content)
		data = {'title': obj.title, "slug": obj.slug, "publish": obj.publish, "content": ""}
		form = PostForm(data=data)
		self.assertFalse(form.is_valid())
		print(form.errors)
		self.assertTrue(form.errors)
		
		





