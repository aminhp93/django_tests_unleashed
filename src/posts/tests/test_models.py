from django.test import TestCase
from django.utils.text import slugify

from posts.models import Post
# Create your tests here.

class PostModelTestCase(TestCase):
	def setUp(self):
		Post.objects.create(title="A new title", slug="this-is-unique-slug")

	def test_post_title(self):
		obj = Post.objects.get(slug="this-is-unique-slug")
		self.assertEqual(obj.title, "A new title")
		self.assertTrue(obj.content == "")

	def create_post(self, title="This title"):
		return Post.objects.create(title=title)

	def test_post_slug(self):
		# generate slug
		title1 = "another title abc"
		title2 = "another title abc"
		slug1 = slugify(title1)
		slug2 = slugify(title2)
		obj1 = self.create_post(title=title1)
		obj2 = self.create_post(title=title2)
		self.assertEqual(obj1.slug, slug1)
		self.assertNotEqual(obj2.slug, slug2)





