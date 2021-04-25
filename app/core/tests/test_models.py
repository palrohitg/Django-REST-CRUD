from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = "rohit@gmail.com"
        password = "Testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test meails for a user normalized"""
        email = "rohit@TEST.COM"
        user = get_user_model().objects.create_user(email, 'test1233')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """When new user not pass emails raise error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test12313')

    def test_create_new_superuser(self):
        """Create a user new super user"""

        user = get_user_model().objects.create_superuser(
            'newSuper@gmail.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
