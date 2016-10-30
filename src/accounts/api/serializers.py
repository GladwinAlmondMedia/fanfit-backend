from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework.serializers import (
		CharField,
		EmailField,
		ModelSerializer, 
		HyperlinkedIdentityField, 
		SerializerMethodField,
		ValidationError
		)

from accounts.models import UserProfile, Address
from competitions.models import FootballClub, Activity

User = get_user_model()

class UserSerializer(ModelSerializer):
	email = EmailField(label="Email address")
	class Meta:
		model = User
		fields = [
			'id',
			'username',
			'email',
			'password',
			'first_name',
			'last_name'
		]
		extra_kwargs = {"password":
							{"write_only": True}
		}

	def validate_email(self, value):
		user_qs = User.objects.filter(email=value)
		if user_qs.exists():
			raise ValidationError("A user with that email address already exists.")
		return value


class AddressSerializer(ModelSerializer):
	class Meta:
		model = Address

class ActivitySerializer(ModelSerializer):
	class Meta:
		model = Activity

		fields = ['id',]

class FootballClubSerializer(ModelSerializer):
	class Meta:
		model = FootballClub

		fields = ['id','club']

class UserProfileSerializer(ModelSerializer):

	user = UserSerializer()
	address = AddressSerializer()
	activity = ActivitySerializer(required=False)
	football_club = FootballClubSerializer()
	# photo = SerializerMethodField()

	class Meta:
		model = UserProfile

	def create(self, validated_data):
		# Create User
		user_obj = User.objects.create(**validated_data['user'])
		user_obj.set_password(validated_data['user']['password'])
		user_obj.save()

		# Create Address
		address_obj = Address.objects.create(**validated_data['address'])

		# Create User Profile
		club_name = validated_data['football_club']["club"]
		football_club = FootballClub.objects.get(club=club_name)
		# football_club = validated_data['football_club']

		gender = validated_data['gender']
		birth_date = validated_data['birth_date']
		weight = validated_data['weight']
		# photo = validated_data['photo']

		profile_obj = UserProfile(
					user = user_obj,
					address = address_obj,
					football_club = football_club,
					gender = gender,
					birth_date = birth_date,
					weight = weight,
					# photo = photo,
					allowed_club_change = True,
					total_points = 0
					)
		profile_obj.save()
		return validated_data

	# def get_photo(self, obj):
	# 	photo = obj.photo
	# 	return self.context['request'].build_absolute_uri(photo)

class UpdateUserProfileSerializer(ModelSerializer):
	activity = ActivitySerializer(required=False)

	football_club = FootballClubSerializer(required=False)

	class Meta:
		model = UserProfile

		fields = ['weight', 'photo', 'football_club', 'activity', 'allowed_club_change', 'total_points']


class UpdateUserSerializer(ModelSerializer):

	class Meta:
		model = User

		fields = ['username', 'first_name', 'last_name',]

class ForgotPasswordSerializer(ModelSerializer):
	class Meta:
		model = User

		fields = ['password']

	def update(self, instance, validated_data):
		instance.set_password(validated_data['password'])
		instance.save()
		return instance

class UpdatePhotoSerializer(ModelSerializer):

	class Meta:
		model = UserProfile

		fields = ['photo']















