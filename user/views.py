from django.shortcuts import render
from .models import UserTeam, Profile
from rest_framework.viewsets import generics, mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserTeamSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from fantasy.models import Player, Team
from django.http import JsonResponse
from rest_framework import status

# Create your views here.
def squad_view(request):
    context = {}
    try:        
        profile = Profile.objects.get(user=request.user)
        try:
            squad = UserTeam.objects.get(user_id=profile.id)
            print(squad.player.all())
            context['objects'] = squad
        except UserTeam.DoesNotExist:
            pass
    except Profile.DoesNotExist:
        pass

    return render(request, "user/squad.html", context)

class UserTeamListViewSet(generics.ListAPIView, mixins.CreateModelMixin):
    serializer_class = UserTeamSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination 
    parser_classes = [JSONParser]
    renderer_classes = [JSONRenderer]
    queryset = UserTeam.objects.all()
    
    def post(self, request):
        
        try:
            
            profile = Profile.objects.get(user=request.user)
            team = UserTeam.objects.get(user_id=profile)
            try:
                player = Player.objects.get(code=request.data['code'])
                if team.player.count() >11:
                    return Response({"error_message":"you cannot choose more than 11 players"}, status=status.HTTP_202_ACCEPTED)
                if team.player.contains(player):
                    return Response({"error_message":f"You already have {player} in your squad"}, status=status.HTTP_202_ACCEPTED)
                team.player.add(player)

                return Response({"message":"player added to squad list"}, status=status.HTTP_202_ACCEPTED)                
                
            except Player.DoesNotExist:
                return Response({"error_message":"player does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        except UserTeam.DoesNotExist:
            team_list = []
            for i in Team.objects.all():
                team_list.append(i.name)
            context = {
                "error":"User must created a squad first!",
                "team": team_list,
            }
            return JsonResponse(context, safe=False)
        
        return Response({"message":"created"})
    

class CreateUserTeamViewSet(generics.ListAPIView, mixins.CreateModelMixin):
    serializer_class = UserTeamSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination 
    parser_classes = [JSONParser]
    renderer_classes = [JSONRenderer]
    queryset = UserTeam.objects.all()
    
    def post(self, request):
        
        request.data["user_id"] = request.user.id
        request.data["team_id"] = Team.objects.get(name=request.data["team_id"]).id
        
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"created"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)