# from django.conf.urls import url
# from django.utils.translation import ugettext_lazy as _
# from .views import UserRegisterView, UserLoginView
#
#
# urlpatterns = [
#     url(_(r'^register/$'),
#         UserRegisterView.as_view(),
#         name='register'),
#     url(_(r'^login/$'),
#         UserLoginView.as_view(),
#         name='login'),
# ]

from django.urls import re_path
from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from .views import (
    RegisterUsers,
    ResetUserPassword,
    LoginUser,
    LogoutUser
)

urlpatterns = [
    url(_(r'^register/$'),
        RegisterUsers.as_view(),
        name='register'),
    url(_(r'^login/$'),
        LoginUser.as_view(),
        name='login'),
    url(_(r'^logout/$'),
        LogoutUser.as_view(),
        name='logout'),
    url(_(r'^reset-password/$'),
        ResetUserPassword.as_view(),
        name='reset'),
]

# from rest_framework.urlpatterns import format_suffix_patterns
#
# app_name = 'shop_list_api'
#
# urlpatterns = format_suffix_patterns([
#     re_path('^auth/register/$',
#             RegisterUsers.as_view(),
#             name='api-register-user'),
#
#     re_path('^auth/reset-password/$',
#             ResetUserPassword.as_view(),
#             name='api-reset-password'),
#
#     re_path('^auth/login/$',
#             LoginUser.as_view(),
#             name='api-login-user'),
#
#     re_path('^auth/logout/$',
#             LogoutUser.as_view(),
#             name='api-logout-user'),
#
#     re_path('^list/users/$',
#             ListAllUsers.as_view(),
#             name='api-all-users'),
#
#     re_path('^users/(?P<username>[\w.@+-]+)/$',
#             SingleUserDetails.as_view(),
#             name='api-user'),
# ])
