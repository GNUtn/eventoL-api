import unittest
from django.contrib.auth.models import User
from api.tests.test_api import api_test


# Django Models
@api_test()
class TestApiUser():
    str_model = 'auth.User'
    model = User
    url_base = '/api/users/'
    filter_fields = ['username', 'email', 'is_staff']
    example = {
        'username': 'Example username',
        'email': 'exaple@example.com',
        'is_staff': True
    }


if __name__ == '__main__':
    unittest.main()
