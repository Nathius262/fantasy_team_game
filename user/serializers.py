from rest_framework import serializers
from .models import UserTeam
from fantasy.serializers import PlayerSerializer

class UserTeamSerializer(serializers.ModelSerializer):
    player = PlayerSerializer(many=True, required=False)
    class Meta:
        model = UserTeam
        exclude = ['id']