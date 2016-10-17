from django.conf.urls import url
from django.contrib import admin

from .views import CompetitionAPIView, ListWorkoutAPIView, CreateWorkoutAPIView

urlpatterns = [
	url(r'^club/(?P<club_id>\d+)/$', CompetitionAPIView.as_view(), name='club-competition'),
	url(r'^workouts/(?P<user_id>\d+)/$', ListWorkoutAPIView.as_view(), name='workout'),
	url(r'^new-workout/user/(?P<user_id>\d+)/activity/(?P<activity_id>\d+)/$', CreateWorkoutAPIView.as_view(), name='new-workout'),
]