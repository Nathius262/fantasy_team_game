from django.contrib import admin
from .models import Player, PlayerTeam, Team, Match

# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'point']
    
    
class PlayerTeamAdmin(admin.ModelAdmin):
    list_display = ['player_id', 'team_id']
 
   
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    

class MatchAdmin(admin.ModelAdmin):
    list_display = ['home_team', 'away_team', 'home_team_score', 'away_team_score', "played_at"]
    

admin.site.register(Player, PlayerAdmin)
admin.site.register(PlayerTeam, PlayerTeamAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Match, MatchAdmin)