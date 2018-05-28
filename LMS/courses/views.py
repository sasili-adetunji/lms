
from rest_framework import status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView
from . import utils
from .serializers import CourseSerializer
from .models import Course


# returning course list
class CourseList(APIView):
    serializer_class = CourseSerializer
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination

    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()
        # print(courses)
        courses_serializer = CourseSerializer(courses, context={'request': request}, many=True)
        return Response(courses_serializer.data)

    def post(self, request):
        if not request.user.is_superuser:
            return Response('Your are not authorize to perform this action', status=status.HTTP_400_BAD_REQUEST)

        courses_serializer = CourseSerializer(data=request.POST, context={'request': request})
        if courses_serializer.is_valid():
            courses_serializer.save()
        else:
            return Response(courses_serializer.errors)
        return Response(courses_serializer.data)


class CourseDetails(APIView):
    serializer_class = CourseSerializer
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        courses = utils.get_course_object(id)
        courses_serializer = CourseSerializer(courses, context={'request': request})
        return Response(courses_serializer.data)

    def put(self, request, id):
        if not request.user.is_superuser:
            return Response('Your are not authorize to perform this action', status=status.HTTP_400_BAD_REQUEST)

        try:
            course = utils.get_course_object(id)
            course = utils.update_course(course, request.data)
        except Exception as e:
            return Response('Server Side error Occured.', status=status.HTTP_400_BAD_REQUEST)

        return Response(CourseSerializer(course).data)

    def delete(self, request, id):
        if not request.user.is_superuser:
            return Response('Your are not authorize to perform this action', status=status.HTTP_400_BAD_REQUEST)

        course = utils.get_course_object(id)
        course.hidden = True
        course.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
