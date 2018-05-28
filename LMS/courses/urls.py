from django.conf.urls import url

from .views import (
                    CourseDetails,
                    CourseList,
                    )


urlpatterns = [
    url(r'^details/(?P<pk>[^/]+)/$', CourseDetails.as_view(), name='course-details'),
    url(r'^list/$', CourseList.as_view(), name='course-list'),

]
