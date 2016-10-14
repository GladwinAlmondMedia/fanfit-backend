from django.conf.urls import url
from django.contrib import admin

from .views import (
	# UserCreateAPIView,
	# UserLoginAPIView,
	UserProfileAPIView,
	UserProfileCreateAPIView,
	UpdateUserProfileAPIView,
	UpdateUserAPIView,
	UpdateUserAddressAPIView,
	ForgotPasswordAPIView
	)

urlpatterns = [

	# url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
	# url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
	url(r'^user-profile/$', UserProfileAPIView.as_view(), name='user-profile'),
	url(r'^create-profile/$', UserProfileCreateAPIView.as_view(), name='create-profile'),
	url(r'^update/profile/(?P<id>\d+)/$', UpdateUserProfileAPIView.as_view(), name='update-profile'),
	url(r'^update/user/(?P<id>\d+)/$', UpdateUserAPIView.as_view(), name='update-user'),
	url(r'^update/address/(?P<id>\d+)/$', UpdateUserAddressAPIView.as_view(), name='update-address'),
	url(r'^update/password/(?P<id>\d+)/$', ForgotPasswordAPIView.as_view(), name='update-password'),
]