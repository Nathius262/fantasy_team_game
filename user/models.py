from django.db import models
from authentication.models import CustomUser

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name="users", on_delete=models.CASCADE, related_name="user_profile")
    
    def __str__(self):
        return self.user.username