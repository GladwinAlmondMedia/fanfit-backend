from django.contrib import admin

# Register your models here.
from .models import ActivityCategory, Activity, Workout, FootballClub, TopCompetitors
from accounts.models import UserProfile

class ActivityAdmin(admin.ModelAdmin):
	def get_queryset(self, request):
		qs = super(ActivityAdmin, self).get_queryset(request)
		current_user = request.user
		if current_user.is_superuser:
			return qs
		profie_qs = UserProfile.objects.get(user=current_user)
		return qs.filter(football_club=profie_qs.football_club)	

admin.site.register(ActivityCategory)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Workout)
admin.site.register(FootballClub)
admin.site.register(TopCompetitors)