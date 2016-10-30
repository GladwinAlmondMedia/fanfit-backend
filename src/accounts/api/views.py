from django.contrib.auth import get_user_model

from rest_framework import authentication

from rest_framework.filters import (
		SearchFilter,
	)
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, UpdateAPIView

from rest_framework.permissions import (
		AllowAny,
		IsAuthenticated,
		IsAdminUser,
		IsAuthenticatedOrReadOnly,
	)

from rest_framework.parsers import FileUploadParser, MultiPartParser

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from rest_framework.views import APIView

from accounts.models import UserProfile, Address
from competitions.models import FootballClub, Activity
from .serializers import (
			# UserCreateSerializer, 
			# UserLoginSerializer, 
			UserSerializer, 
			UserProfileSerializer, 
			UpdateUserProfileSerializer, 
			UpdateUserSerializer, 
			AddressSerializer,
			ForgotPasswordSerializer,
			UpdatePhotoSerializer 
		)

User = get_user_model()


class UserProfileAPIView(RetrieveAPIView):

	authentication_classes = (authentication.TokenAuthentication,)
	serializer_class = UserProfileSerializer

	def get(self, request, format=None):
		queryset = UserProfile.objects.get(user=request.user)
		serializer = UserProfileSerializer(queryset, context={'request': request})
		return Response(serializer.data)

class UserProfileCreateAPIView(CreateAPIView):
	serializer_class = UserProfileSerializer
	queryset = UserProfile.objects.all()

	def get(self, request, format=None):
		queryset = UserProfile.objects.all()
		serializer = UserProfileSerializer(queryset, context={'request': request})
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=HTTP_200_OK)
		else:
			print(serializer.errors)
			return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class UpdateUserAPIView(RetrieveUpdateAPIView):
	queryset = User.objects.all()
	serializer_class = UpdateUserSerializer
	lookup_field = 'id'

class UpdateUserProfileAPIView(RetrieveUpdateAPIView):
	queryset = UserProfile.objects.all()
	serializer_class = UpdateUserProfileSerializer

	lookup_field = 'id'

	def perform_update(self, serializer):
		activity_id = self.kwargs['activity_id']
		if activity_id == '0':
			activity = None
		else:
			activity = Activity.objects.get(id=activity_id)
			queryset = UserProfile.objects.all()
		instance = serializer.save(activity=activity)

class UpdateUserAddressAPIView(RetrieveUpdateAPIView):
	queryset = Address.objects.all()
	serializer_class = AddressSerializer
	lookup_field = 'id'

class ForgotPasswordAPIView(RetrieveUpdateAPIView):
	queryset = User.objects.all()
	serializer_class = ForgotPasswordSerializer
	lookup_field = 'id'

class UpdatePhotoAPIView(UpdateAPIView):

	# parser_classes = (MultiPartParser,)

	queryset = UserProfile.objects.all()
	serializer_class = UpdatePhotoSerializer
	lookup_field = 'id'

	def put(self, request, id, format=None):
		queryset = UserProfile.objects.get(id=id)
		serializer = UpdatePhotoSerializer(queryset, data=request.data, context={'request': request})
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=HTTP_200_OK)
		else:
			print(serializer.errors)
			return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)








