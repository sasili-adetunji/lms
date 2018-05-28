
from django.http import Http404
from .models import Course


def get_course_object(title):
    try:
        return Course.objects.get(title=title)
    except Course.DoesNotExist:
        raise Http404


def update_course(course, request_data):
    course.title = request_data.get('title', course.title)
    course.description = request_data.get('description', course.description)
    course.start_date = request_data.get('date_added', course.date_added)
    course.save()
    return course
