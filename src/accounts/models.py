from django.db import models

# Create your models here.
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from competitions.models import Activity, FootballClub

def upload_location(instance, filename):
	return "%s/%s" %(instance.id, filename)

class Address(models.Model):
	address_line_1 = models.CharField(max_length=60)
	address_line_2 = models.CharField(max_length=60, null=True, blank=True)
	town_city = models.CharField(max_length=60)
	county = models.CharField(max_length=60, null=True, blank=True)
	postcode = models.CharField(max_length=10)

	def __str__(self):
		return self.address_line_1

class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name='user')
	football_club = models.ForeignKey(FootballClub, null=False, blank=False)
	GENDERS = (("Male", "Male",),("Female", "Female"))
	gender = models.CharField(max_length=10, choices=GENDERS)
	birth_date = models.DateField()
	weight = models.IntegerField()
	address = models.OneToOneField(Address, on_delete=models.CASCADE)
	photo = models.ImageField(upload_to=upload_location, null=True, blank=True)
	activity = models.ForeignKey(Activity, null=True, blank=True)
	allowed_club_change = models.BooleanField(default=True)
	total_points = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True, null=True)


	def __str__(self):
		user = self.user
		return "%ss Profile" %user

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

        