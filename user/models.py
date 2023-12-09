from django.db import models
from authentication.models import CustomUser
from fantasy.models import Team, Player
from django.core.exceptions import ValidationError

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, verbose_name="users", on_delete=models.CASCADE, related_name="user_profile")
    
    def __str__(self):
        return self.user.username
    


    
class UserTeam(models.Model):
    user_id = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True, blank=False)
    my_team = models.CharField(max_length=225, null=True, blank=False)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=False)
    player = models.ManyToManyField(Player, blank=True, related_name="user_player")
    
    def __str__(self):
        return str(self.user_id)
    