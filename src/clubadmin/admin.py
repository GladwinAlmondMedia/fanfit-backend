from django.contrib import admin

from django import forms

# Register your models here.
from .models import Competition

from competitions.models import Activity
from accounts.models import UserProfile

# class CompetitionAdminForm(forms.ModelForm):

# 	class Meta:
# 		model = Competition

# 		fields = '__all__'

# 	def __init__(self, *args, **kwargs):
# 		super(CompetitionAdminForm, self).__init__(*args, **kwargs)
# 		self.fields['current_walking_activity'].queryset = Activity.objects.filter(football_club=self.instance.football_club)

class CompetitionAdmin(admin.ModelAdmin):
	# form = CompetitionAdminForm

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if 'activity' in db_field.name:
			current_user = request.user
			profile_qs = UserProfile.objects.get(user=current_user)
			kwargs["queryset"] = Activity.objects.filter(football_club=profile_qs.football_club)
		return super(CompetitionAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Competition, CompetitionAdmin)