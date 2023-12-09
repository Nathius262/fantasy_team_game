from django.contrib import admin
from .models import Profile, UserTeam

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user',]
    

class UserTeamAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'team_id']
    
    
class LimitedM2MThroughModelAdmin(admin.ModelAdmin):
    list_display = ['user_team', 'player_name']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(UserTeam, UserTeamAdmin)
#admin.site.register(LimitedM2MThroughModel, LimitedM2MThroughModelAdmin)