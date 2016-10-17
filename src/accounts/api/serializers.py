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
from competitions.models import FootballClub

User = get_user_model()

# class UserCreateSerializer(ModelSerializer):
# 	email = EmailField(label='Email Address')
# 	email2 = EmailField(label='Confirm Email')
# 	class Meta:
# 		model = User
# 		fields = [
# 			'username',
# 			'email',
# 			'email2',
# 			'password',
			
# 		]
# 		extra_kwargs = {"password":
# 							{"write_only": True}
# 		}

# 	def validate_email(self, value):
# 		data = self.get_initial()
# 		email2 = data.get("email2")
# 		email1 = value
# 		if email1 != email2:
# 			raise ValidationError("Emails must match.")

# 		user_qs = User.objects.filter(email=email1)
# 		if user_qs.exists():
# 			raise ValidationError("This user has already registered.")

# 		return value

# 	def validate_email2(self, value):
# 		data = self.get_initial()
# 		email1 = data.get("email")
# 		email2 = value
# 		if email1 != email2:
# 			raise ValidationError("Emails must match.")
# 		return value

# 	def create(self, validated_data):
# 		username = validated_data['username']
# 		email = validated_data['email']
# 		password = validated_data['password']

# 		user_obj = User(
# 				username = username,
# 				email = email,
# 			)
# 		user_obj.set_password(password)
# 		user_obj.save()
# 		return validated_data


# class UserLoginSerializer(ModelSerializer):
# 	token = CharField(allow_blank=True, read_only=True)
# 	username = CharField(required=False, allow_blank=True)
# 	email = EmailField(label='Email Address', required=False, allow_blank=True)
# 	class Meta:
# 		model = User
# 		fields = [
# 			'token',
# 			'username',
# 			'email',
# 			'password',
# 		]
# 		extra_kwargs = {"password":
# 							{"write_only": True}
# 		}

# 	def validate(self, data):
# 		user_obj = None
# 		email = data.get("email", None)
# 		username = data.get("username", None)
# 		password = data["password"]
# 		if not email and not username:
# 			raise ValidationError("A username or email is required to login.")

# 		user = User.objects.filter(
# 				Q(email=email) |
# 				Q(username=username)
# 			).distinct()
# 		user = user.exclude(email__isnull=True).exclude(email__iexact='')

# 		if user.exists() and user.count() == 1:
# 			user_obj = user.first()
# 		else:
# 			raise ValidationError("This username/email is not valid.")

# 		if user_obj:
# 			if not user_obj.check_password(password):
# 				raise ValidationError("Incorrect password")
# 		return data

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

class UserProfileSerializer(ModelSerializer):

	user = UserSerializer()
	address = AddressSerializer()

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
		football_club = validated_data['football_club']
		gender = validated_data['gender']
		birth_date = validated_data['birth_date']
		weight = validated_data['weight']
		photo = validated_data['photo']

		profile_obj = UserProfile(
					user = user_obj,
					address = address_obj,
					football_club = football_club,
					gender = gender,
					birth_date = birth_date,
					weight = weight,
					photo = photo,
					)
		profile_obj.save()
		return validated_data

class UpdateUserProfileSerializer(ModelSerializer):
	class Meta:
		model = UserProfile

		fields = ['weight', 'photo', 'football_club', 'activity', 'allowed_club_change']


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














