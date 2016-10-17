from django.contrib.auth import get_user_model

from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView
from rest_framework.response import Response


from .serializers import CompetitionSerializer, WorkoutSerializer
from clubadmin.models import Competition

from competitions.models import FootballClub, Workout, Activity

from accounts.models import UserProfile

User = get_user_model()

class CompetitionAPIView(RetrieveAPIView):

	serializer_class = CompetitionSerializer
	lookup_field = 'club_id'

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
		user_id = self.kwargs['user_id']
		activity_id = self.kwargs['activity_id']
		user = User.objects.get(id=user_id)
		activity = Activity.objects.get(id=activity_id)
		queryset = Workout.objects.all()
		instance = serializer.save(user=user, activity=activity)
		user_profile = UserProfile.objects.get(user=user)
		total_points = user_profile.total_points
		new_points = instance.points_tally
		total_points += new_points
		user_profile.total_points = total_points
		user_profile.save()







