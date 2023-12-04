from django.db import models
from authentication.models import CustomUser
from fantasy.models import Team

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, verbose_name="users", on_delete=models.CASCADE, related_name="user_profile")
    
    def __str__(self):
        return self.user.username
    
class UserTeam(models.Model):
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=False)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=False)
    
    def __str__(self):
        return self.user_id
    