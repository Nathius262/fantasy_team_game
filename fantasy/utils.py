import requests
import json
from fantasy.models import Team, Player, PlayerTeam
import os

def getPremierShipData():
    # URL of the API providing JSON data
    url = "https://fantasy.premierleague.com/api/bootstrap-static/"

    # Make a GET request
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON data
        json_data = response.json()
        
        #add team to the database
        for data in json_data["teams"]:
            Team.objects.get_or_create(name=data["name"], code=data["code"], cid=data["id"])
            
            
        for data in json_data["elements"]:
            
            player, created = Player.objects.get_or_create(code=data["code"], cid=data["id"])
            team = Team.objects.get(cid=data["team"], code=data["team_code"])
            if not created:
                PlayerTeam.objects.get_or_create(player_id=player, team_id=team)
            else:
                player.name = f'{data["first_name"]} {data["second_name"]}'
                player.point= data["total_points"]
                PlayerTeam.objects.get_or_create(player_id=player, team_id=team)
                
                index_range = 0
                data_range = data['element_type']
                if data_range == 1:
                    data_range = index_range
                elif data_range == 2:
                    data_range =1
                elif data_range == 3:
                    data_range = 2
                else:
                    data_range = 3
                
                    
                
                player.position = json_data["element_types"][data_range]["plural_name_short"]
                
                player.save()
            
        """ # Save the JSON data to a file
        with open("premiership.json", "w") as json_file:
            data = json.dump(json_data, json_file, indent=4)"""
            

        #print("JSON data saved to output.json")
    else:
        print(f"Error: {response.status_code}")
        
        
    
