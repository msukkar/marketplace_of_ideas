from model_api.models import *

from django.contrib.auth.models import AnonymousUser, User
from django.core.exceptions import ValidationError
from django.test import Client as Robot
from django.test import RequestFactory, TestCase

class UserTests(TestCase):

    def test_blank_username(self):
        user = User(
            first_name="Alan",
            last_name="Wei",
            password='password'
        )
        self.assertRaises(ValidationError, user.full_clean)

    def test_long_username(self):
        user = User(
            username="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",
            first_name="Alan",
            last_name="Wei",
            password='password'
        )
        self.assertRaises(ValidationError, user.full_clean)

    def test_long_first_name(self):
        user = User(
            first_name="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",
            username="Alan",
            last_name="Wei",
            password='password'
        )
        self.assertRaises(ValidationError, user.full_clean)

    def test_long_last_name(self):
        user = User(
            last_name="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",
            first_name="Alan",
            username="Wei",
            password='password'
        )
        self.assertRaises(ValidationError, user.full_clean)

    def test_long_password(self):
        user = User(
            password="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",
            first_name="Alan",
            username="Wei",
            last_name='password'
        )
        self.assertRaises(ValidationError, user.full_clean)

    def test_unique_username(self):
        user = User(
            username='aw3as',
            first_name='Alan',
            last_name='Wei',
            password='password'
        )
        user.save()
        user2 = User(
            username='aw3as',
            first_name='Alan',
            last_name='Wei',
            password='password'
        )
        self.assertRaises(ValidationError, user2.full_clean)

class BlogPostTests(TestCase):

    def testBlankBlogPost(self):
        blogPost = BlogPost()

        self.assertRaises(ValidationError, blogPost.full_clean)

class AuthenticatorTests(TestCase):

    def testBlankUserID(self):
        authenticator = Authenticator(authenticator="abc")

        self.assertRaises(ValidationError, authenticator.full_clean)

    def testLongAuthenticator(self):
        authenticator = Authenticator(user_id=1, authenticator="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")

        self.assertRaises(ValidationError, authenticator.full_clean)