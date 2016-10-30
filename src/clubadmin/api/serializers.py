from django.contrib.auth import get_user_model

from rest_framework.serializers import ModelSerializer, DecimalField, SerializerMethodField

from accounts.models import UserProfile

from clubadmin.models import Competition 

from competitions.models import Activity, FootballClub, Workout, ActivityCategory, TopCompetitors

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

class WorkoutSerializer(ModelSerializer):

	activity = ActivitySerializer(required=False)

	class Meta:
		model = Workout

		exclude = ['user']

class TopUserSerializer(ModelSerializer):

	user_points = SerializerMethodField()

	class Meta:
		model = User

		fields = ['id', 'username', 'user_points']

	def get_user_points(self, obj):
		user_profile = UserProfile.objects.get(user=obj)
		return user_profile.total_points

class TopCompetitorSerializer(ModelSerializer):

	first = TopUserSerializer()
	second = TopUserSerializer()
	third = TopUserSerializer()

	class Meta:
		model = TopCompetitors






















