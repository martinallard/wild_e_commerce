from django.conf.urls import url
from .views import register, profile, logout, login
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete


urlpatterns = [
                url(r'^login', login, name='login'),
                url(r'^logout', logout, name='logout'),
                url(r'^profile', profile, name='profile'),
                url(r'^register', register, name='register'),
                url(r'^password/reset/$', password_reset,
                         {'post_reset_redirect': '/user/password/reset/done/'}, name='password_reset'),
                url(r'^password/reset/done/$', password_reset_done, name='password_reset_done'),
                url(r'^password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
                        password_reset_confirm, {'post_reset_redirect': '/user/password/done/'}, name='password_reset_confirm'),
                url(r'^password/done/$', password_reset_complete, name='password_reset_complete'),
]
