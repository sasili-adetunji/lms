from django.conf.urls import url, include
from django.urls import path
from django.utils.translation import ugettext_lazy as _
from rest_framework.routers import DefaultRouter

from .views import (
    # RegisterUsers,
    # ResetUserPassword,
    # LoginUser,
    LogoutUser,
    UserProfileViewSet,
    LoginViewSet,
)


router = DefaultRouter()

router.register('profile', UserProfileViewSet)
router.register('login', LoginViewSet, base_name='login')  # needs basename coz its not model viewsets

urlpatterns = [
    url(r'', include(router.urls)),
    url(_(r'^logout/$'),
        LogoutUser.as_view(),
        )
]

# urlpatterns += router.urls


# urlpatterns = [
    # url(_(r'^register/$'),
    #     RegisterUsers.as_view(),
    #     name='register'),
    # url(_(r'^login/$'),
    #     LoginUser.as_view(),
    #     name='login'),
    # url(_(r'^logout/$'),
    #     LogoutUser.as_view(),
    #     name='logout'),
    # url(_(r'^profile/$'),
    #     UserProfileViewSet.as_view(),
    #     name='reset'),
    # url(r'', include(router.urls))

# ]
