from django.db import models

from competitions.models import Activity

from competitions.models import FootballClub


# Create your models here.
class Competition(models.Model):
	football_club = models.ForeignKey(FootballClub)

	current_walking_activity = models.ForeignKey(
		Activity, 
		on_delete=models.CASCADE,
		limit_choices_to={'category__category': 'Walking'},
		related_name='current_walking_activity',
		help_text= ("Enter the current walking activiy for competition"), 
		blank=True, 
		null=True
	)
	current_running_activity = models.ForeignKey(
		Activity, 
		on_delete=models.CASCADE, 
		limit_choices_to={'category__category': 'Running'},
		related_name='current_running_activity', 
		blank=True, 
		null=True
	)
	current_cycling_activity = models.ForeignKey(
		Activity, 
		on_delete=models.CASCADE, 
		limit_choices_to={'category__category': 'Cycling'},
		related_name='current_cycling_activity', 
		blank=True, 
		null=True
	)

	next_walking_activity = models.ForeignKey(
		Activity, 
		on_delete=models.CASCADE, 
		limit_choices_to={'category__category': 'Walking'},
		related_name='next_walking_activity', 
		blank=True, 
		null=True
	)
	next_running_activity = models.ForeignKey(
		Activity, 
		on_delete=models.CASCADE, 
		limit_choices_to={'category__category': 'Running'},
		related_name='next_running_activity', 
		blank=True, 
		null=True
	)
	next_cycling_activity = models.ForeignKey(
		Activity, 
		on_delete=models.CASCADE, 
		limit_choices_to={'category__category': 'Cycling'},
		related_name='next_cycling_activity', 
		blank=True, 
		null=True
	)

	def __str__(self):
		return self.football_club.club




















