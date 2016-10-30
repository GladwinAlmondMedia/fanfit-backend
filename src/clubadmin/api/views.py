from django.contrib.auth import get_user_model

from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView
from rest_framework.response import Response


from .serializers import CompetitionSerializer, WorkoutSerializer, FootballClubSerializer, TopCompetitorSerializer
from clubadmin.models import Competition

from competitions.models import FootballClub, Workout, Activity, TopCompetitors

from accounts.models import UserProfile

User = get_user_model()

class CompetitionAPIView(RetrieveAPIView):

	serializer_class = CompetitionSerializer
	lookup_field = 'id'

	# Takes in id of football club and returns accompanying Competition 
	def get(self, request, id, format=None):
		football_club = FootballClub.objects.get(id=id)
		queryset = Competition.objects.get(football_club=football_club)
		serializer = CompetitionSerializer(queryset)
		return Response(serializer.data)

class ListWorkoutAPIView(ListAPIView):
	serializer_class = WorkoutSerializer
	lookup_field = 'user_id'

	# Takes in id of user and returns a list of all their workouts
	def get_queryset(self):
		id = self.kwargs['user_id']
		user = User.objects.get(id=id)
		return Workout.objects.filter(user=user)

class CreateWorkoutAPIView(CreateAPIView):
	serializer_class = WorkoutSerializer
	queryset = Workout.objects.all()

	def perform_create(self, serializer):
		#Create new workout and for user and activity 
		user_id = self.kwargs['user_id']
		activity_id = self.kwargs['activity_id']
		user = User.objects.get(id=user_id)
		activity = Activity.objects.get(id=activity_id)
		queryset = Workout.objects.all()
		instance = serializer.save(user=user, activity=activity)

		#Update users total points for activity
		user_profile = UserProfile.objects.get(user=user)
		total_points = user_profile.total_points
		new_points = instance.points_tally
		total_points += new_points
		user_profile.total_points = total_points
		user_profile.save()

		#Update top competitors
		top_competitors_obj = TopCompetitors.objects.get(activity=activity)

		first_user = top_competitors_obj.first
		second_user = top_competitors_obj.second
		third_user = top_competitors_obj.third

		current_user_points = user_profile.total_points

		if (first_user is not None) and (first_user.id != user.id):
			first_user_profile = UserProfile.objects.get(user=first_user)
			if current_user_points > first_user_profile.total_points:
				third_user = second_user
				second_user = first_user
				first_user = user
			elif (second_user is not None) and (second_user.id != user.id):
				second_user_profile = UserProfile.objects.get(user=second_user)
				if current_user_points > second_user_profile.total_points:
					third_user = second_user
					second_user = user
				elif (third_user is not None) and (third_user.id != user.id):
					third_user_profile = user_profile.objects.get(user=third_user)
					if current_user_points > third_user_profile.total_points:
						third_user = user
				else:
					third_user = user
			else:
				second_user = user
		else:
			first_user = user

		top_competitors_obj.first = first_user
		top_competitors_obj.second = second_user
		top_competitors_obj.third = third_user

		top_competitors_obj.save()


class ListFootballClubAPIView(ListAPIView):
	serializer_class = FootballClubSerializer
	queryset = FootballClub.objects.all()

class TopCompetitorsAPIView(RetrieveAPIView):
	serializer_class = TopCompetitorSerializer
	lookup_field = 'activity_id'

	def  get(self, request, activity_id, format=None):
		activity = Activity.objects.get(id=activity_id)
		queryset = TopCompetitors.objects.get(activity=activity)
		serializer = TopCompetitorSerializer(queryset)
		return Response(serializer.data)







