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
