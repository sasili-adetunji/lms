import json
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from ..models import UserProfile
from ..serializers import CompositeUserSerializer


class BaseTest(APITestCase):
    """
    Base Test for Auth endpoints and models
    """

    client = APIClient()
    token = ""

    def setUp(self):
        # create a admin user
        self.user = User.objects.create_superuser(
            username='test_user',
            email='test@mail.com',
            password='testing',
            first_name='test',
            last_name='user',
        )
        # create a user profile for admin user
        self.user_profile = UserProfile.objects.create(
            user=self.user
        )

        # create a test user with out admin rights
        self.other_user = User.objects.create_user(
            username='other_test_user',
            email='other_test@mail.com',
            password='other_testing',
            first_name='other',
            last_name='user',
        )
        # create a user profile for other test user
        self.other_test_user_profile = UserProfile.objects.create(
            user=self.other_user
        )

        # test data
        self.valid_data = {
            # mandatory
            'username': 'another_test_user',
            'password': 'another',
            # optional
            'email': 'another@mail.com',
            'first_name': 'another',
            'last_name': 'user',
        }

        # if one or more of the mandatory fields is missing,
        # data is invalid
        self.invalid_data = {
            # mandatory
            'username': '',
            'password': '',
            # optional
            'email': 'another@mail.com',
            'first_name': '',
            'last_name': '',
        }

    def login_client(self, username, password):
        # login
        response = self.client.post(
            reverse('create-token'),
            data=json.dumps(
                {
                    'username': username,
                    'password': password
                }
            ),
            content_type='application/json'
        )
        self.token = response.data['token']
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.token
        )
        self.client.login(username=username, password=password)


class AuthBaseTest(BaseTest):

    @staticmethod
    def get_all_expected_user_profiles():
        # get all user profiles in the db and return as a serialized object
        results_queryset = []
        for user in User.objects.all():
            results_queryset.append({
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'last_login': user.last_login,
                'date_joined': user.date_joined
            })
        return CompositeUserSerializer(results_queryset, many=True)

    def get_expected_single_user_profile(self):
        # this returns the test user profile
        serializer = CompositeUserSerializer(
            data={
                'first_name': self.user.first_name,
                'last_name': self.user.last_name,
                'email': self.user.email,
                'last_login': self.user.last_login,
                'date_joined': self.user.date_joined
            }
        )
        serializer.is_valid()
        return serializer
