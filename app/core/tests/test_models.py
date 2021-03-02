from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email(self):
        # Test creating a user with email is successful
        email = 'siriusblack@gmail.com'
        password = 'alirezaw123'
        user = get_user_model().objects.create_user(
            email=email, password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        # Test the user's email is normalized
        email = 'test@LONDONAPPDEV.COM'
        user = get_user_model().objects.create_user(email, 'test123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        # Test creating user with no email raises error
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_super_user(self):
        # Test creating super user
        user = get_user_model().objects.create_superuser(
            'test@londonappdev.com', 'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
