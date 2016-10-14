from django.db import models
from django.conf import settings
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

class Workout(models.Model):
	time = models.IntegerField()
	distance = models.DecimalField(max_digits=5, decimal_places=2)
	average_speed = models.DecimalField(max_digits=5, decimal_places=2)
	calories_burnt = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return self.title
