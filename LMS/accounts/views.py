from rest_framework.response import Response
from rest_framework.views import APIView, status
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny
)
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializers import (
    CompositeUserSerializer,
    TokenSerializer,
    UserSerializer,
    UserProfileSerializer,
)
from .utils import (
    fetch_single_user,
    create_user_profile,
    update_user_profile,
)
from django.contrib.auth import authenticate, login, logout
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


# API endpoint views
class RegisterUsers(APIView):
    """
    View to create a user in the system
    * this is a public view
    * non authenticated users can access it
    """
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def post(self, request):
        """
        Create a new user
        This view function creates/POSTs a new user. A user data is
        stored in two models, i.e, User and UserProfile.
        Therefore the process of creating a user involves two
        steps;
        step 1: create a user account in the django auth User model
        step 2: create a user profile in the UserProfile model
        :param request:
        :return:
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            info = {
                'username': request.data.get('username'),
                'password': request.data.get('password'),
                'first_name': request.data.get('first_name'),
                'last_name': request.data.get('last_name'),
            }
            if create_user_profile(data=info):
                # serialize the created user profile
                serializer = CompositeUserSerializer(
                    data=fetch_single_user(username=info['username'])
                )
                serializer.is_valid()
                return Response(
                    data=serializer.data,
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response({
                    'message': "Error"
                    },
                    status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ResetUserPassword(APIView):
    """
    View to update password of a logged in user
    """
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def put(self, request):
        """
        Update password of the user in the request object
        :param request:
        :return:
        """
        data = {
            'username': request.user.username,
            'password': request.data.get('password', '')
        }
        if update_user_profile(data=data):
            return Response({"message": "Your password has been successfully updated"}, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class LoginUser(APIView):
    """
    View to login a user
    returns a token
    """
    permission_classes = (AllowAny,)
    serializer_class = UserProfileSerializer

    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login saves the user’s ID in the session,
            # using Django’s session framework.
            login(request, user)
            serializer = TokenSerializer(data={
                # using drf jwt utility functions to generate a token
                'token': jwt_encode_handler(
                    jwt_payload_handler(user)
                )})
            serializer.is_valid()

            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class LogoutUser(APIView):
    """
    View to logout a user.
    * You have to have logged in to be able logout
    """

    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        logout(request)
        return Response({
                        "message": "You have successfully logout of the application"},
                        status=status.HTTP_200_OK)
