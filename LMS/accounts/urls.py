from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _
from .views import UserRegisterView, UserLoginView


urlpatterns = [
    url(_(r'^register/$'),
        UserRegisterView.as_view(),
        name='register'),
    url(_(r'^login/$'),
        UserLoginView.as_view(),
        name='login'),
]
