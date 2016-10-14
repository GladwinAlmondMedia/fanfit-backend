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

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from rest_framework.views import APIView

from accounts.models import UserProfile, Address
from competitions.models import FootballClub
from .serializers import (
			# UserCreateSerializer, 
			# UserLoginSerializer, 
			UserSerializer, 
			UserProfileSerializer, 
			UpdateUserProfileSerializer, 
			UpdateUserSerializer, 
			AddressSerializer,
			ForgotPasswordSerializer 
		)

User = get_user_model()


# class UserCreateAPIView(CreateAPIView):
# 	serializer_class = UserCreateSerializer
# 	queryset = User.objects.all()



# class UserLoginAPIView(APIView):
# 	permission_classes = [AllowAny]
# 	serializer_class = UserLoginSerializer


# 	def post(self, request, *args, **kwargs):
# 		data = request.data
# 		serializer_class = UserLoginSerializer(data=data)
# 		serializer = UserLoginSerializer(data=data)
# 		if serializer.is_valid(raise_exception=True):
# 			new_data = serializer.data
# 			return Response(new_data, status=HTTP_200_OK)
# 		return response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UserProfileAPIView(RetrieveAPIView):

	authentication_classes = (authentication.TokenAuthentication,)
	serializer_class = UserProfileSerializer

	def get(self, request, format=None):
		queryset = UserProfile.objects.get(user=request.user)
		serializer = UserProfileSerializer(queryset)
		return Response(serializer.data)

class UserProfileCreateAPIView(CreateAPIView):
	serializer_class = UserProfileSerializer
	queryset = UserProfile.objects.all()

class UpdateUserAPIView(RetrieveUpdateAPIView):
	queryset = User.objects.all()
	serializer_class = UpdateUserSerializer
	lookup_field = 'id'

class UpdateUserProfileAPIView(RetrieveUpdateAPIView):
	queryset = UserProfile.objects.all()
	serializer_class = UpdateUserProfileSerializer
	lookup_field = 'id'

class UpdateUserAddressAPIView(RetrieveUpdateAPIView):
	queryset = Address.objects.all()
	serializer_class = AddressSerializer
	lookup_field = 'id'

class ForgotPasswordAPIView(RetrieveUpdateAPIView):
	queryset = User.objects.all()
	serializer_class = ForgotPasswordSerializer
	lookup_field = 'id'









