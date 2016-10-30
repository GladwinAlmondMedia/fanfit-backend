from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone

# Create your models here.

class FootballClub(models.Model):
	club = models.CharField(max_length=120)

	def __str__(self):
		return self.club

class ActivityCategory(models.Model):
	category = models.CharField(max_length=120)

	def __str__(self):
		return self.category

class Activity(models.Model):
	category = models.ForeignKey(ActivityCategory)
	football_club = models.ForeignKey(FootballClub)
	title = models.CharField(max_length=120)
	details = models.TextField(max_length=1000, blank=True, null=True)
	start_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)   # Remove default
	end_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)
	prize = models.CharField(max_length=120)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.title

class TopCompetitors(models.Model):
	activity = models.ForeignKey(Activity)
	first = models.ForeignKey(User, related_name='first_top_user', blank=True, null=True)
	second = models.ForeignKey(User, related_name='second_top_user', blank=True, null=True)
	third = models.ForeignKey(User, related_name='third_top_user', blank=True, null=True)

	def __str__(self):
		return "%s's top competitors" %self.activity

@receiver(post_save, sender=Activity)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		TopCompetitors.objects.create(activity=instance)


class Workout(models.Model):
	user = models.ForeignKey(User, related_name='workout_user')
	activity = models.ForeignKey(Activity)
	points_tally = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True, null=True)
	total_time = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True, null=True)
	total_distance = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True, null=True)
	average_speed = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True, null=True)
	total_calories_burned = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True, null=True)

	def __str__(self):
		user = self.user
		activity = self.activity
		return "%s - %s" %(user, activity)

