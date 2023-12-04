from django.contrib import admin
from .models import Player, PlayerTeam, Team, Match, Premiership
from django.contrib import messages
from django.utils.translation import ngettext
from.utils import getPremierShipData

# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'point']
    
    
class PlayerTeamAdmin(admin.ModelAdmin):
    list_display = ['player_id', 'team_id']
 
   
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    

class MatchAdmin(admin.ModelAdmin):
    list_display = ['home_team', 'away_team', 'home_team_score', 'away_team_score', "played_at"]
    

class PremiershipAdmin(admin.ModelAdmin):
    actions = ['run_my_function']
    def run_my_function(self, request, queryset):
        updated = queryset.update(run_data=False)
        getPremierShipData()
        print("working admin")
        self.message_user(
            request,
            ngettext(
                "%d story was successfully marked as published.",
                "%d stories were successfully marked as published.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

admin.site.register(Player, PlayerAdmin)
admin.site.register(PlayerTeam, PlayerTeamAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Premiership, PremiershipAdmin)