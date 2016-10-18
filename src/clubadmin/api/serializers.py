from django.contrib.auth import get_user_model

from rest_framework.serializers import ModelSerializer

from clubadmin.models import Competition 

from competitions.models import Activity, FootballClub, Workout, ActivityCategory

User = get_user_model()

class ActivityCategorySerializer(ModelSerializer):
	class Meta:
		model = ActivityCategory

class ActivitySerializer(ModelSerializer):
	category = ActivityCategorySerializer()
	class Meta:
		model = Activity

class FootballClubSerializer(ModelSerializer):
	class Meta:
		model = FootballClub

class CompetitionSerializer(ModelSerializer):

	football_club = FootballClubSerializer()

	current_walking_activity = ActivitySerializer()
	current_running_activity = ActivitySerializer()
	current_cycling_activity = ActivitySerializer()
	next_walking_activity = ActivitySerializer()
	next_running_activity = ActivitySerializer()
	next_cycling_activity = ActivitySerializer()	

	class Meta:
		model = Competition

class WorkoutActivitySerializer(ModelSerializer):
	class Meta:
		model = Activity

class WorkoutSerializer(ModelSerializer):

	activity = ActivitySerializer(required=False)

	class Meta:
		model = Workout

		exclude = ['user']






















