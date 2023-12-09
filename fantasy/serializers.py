from rest_framework import serializers
from .models import Player, PlayerTeam

class PlayerTeamSerializer(serializers.ModelSerializer):
    team_id = serializers.SerializerMethodField("get_team")
    player = serializers.SerializerMethodField("get_player")
    position = serializers.SerializerMethodField("get_position")
    point = serializers.SerializerMethodField("get_point")
    code = serializers.SerializerMethodField("get_code")
    
    class Meta:
        model = PlayerTeam
        
        #fields = '__all__'
        exclude = ['id',]
        
    def get_team(self, obj):
        return obj.team_id.name
    
    def get_player(self, obj):
        return obj.player_id.name
    
    def get_position(self, obj):
        return obj.player_id.position
    
    def get_point(self, obj):
        return obj.player_id.point
    
    def get_code(self, obj):
        return obj.player_id.code
    
    
class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        
        #fields = '__all__'
        exclude = ['id',]
        

    