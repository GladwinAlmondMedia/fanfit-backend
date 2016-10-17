from django.contrib import admin

# Register your models here.
from .models import Address, UserProfile

class UserProfileAdmin(admin.ModelAdmin):
	exclude = ('workout_stats',)

admin.site.register(Address)
admin.site.register(UserProfile, UserProfileAdmin)