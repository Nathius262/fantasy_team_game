from django.db import models


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=225, null=True, blank=False)
    cid = models.CharField(max_length=20, unique=True, null=True, blank=False)
    code =models.CharField(max_length=20, unique=True, null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=False)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=225, null=True, blank=False)
    cid = models.CharField(max_length=50, unique=True, null=True, blank=False)
    code = models.CharField(max_length=50, unique=True, null=True, blank=False)
    position = models.CharField(max_length=225, null=True, blank=False)
    point = models.DecimalField(max_digits=12, decimal_places=2, null=True)

    def __str__(self):
        return self.name


class PlayerTeam(models.Model):
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, blank=False, related_name="player_team")
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=False)

    def __str__(self):
        return str(self.player_id)


class Match(models.Model):
    home_team = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, blank=False, related_name="home_team")
    away_team = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, blank=False, related_name="away_team")
    home_team_score = models.DecimalField(max_digits=5, decimal_places=2)
    away_team_score = models.DecimalField(max_digits=5, decimal_places=2)
    played_at = models.CharField(max_length=225, null=True, blank=False)

    class Meta:
        verbose_name_plural = "matches"


    def __str__(self):
        return self.home_team


class Premiership(models.Model):
    # Your model fields here
    run_data = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
