from django.conf.urls import url
from django.contrib import admin

from .views import CompetitionAPIView, ListWorkoutAPIView, CreateWorkoutAPIView, ListFootballClubAPIView, TopCompetitorsAPIView

urlpatterns = [
	url(r'^club/(?P<id>\d+)/$', CompetitionAPIView.as_view(), name='club-competition'),
	url(r'^workouts/(?P<user_id>\d+)/$', ListWorkoutAPIView.as_view(), name='workout'),
	url(r'^new-workout/user/(?P<user_id>\d+)/activity/(?P<activity_id>\d+)/$', CreateWorkoutAPIView.as_view(), name='new-workout'),
	url(r'^football-clubs/$', ListFootballClubAPIView.as_view(), name='list-clubs'),
	url(r'^top-competitors/(?P<activity_id>\d+)/$', TopCompetitorsAPIView.as_view(), name='top-competitors'),
]