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
            player, created = Player.objects.get_or_create(name=f'{data["first_name"]} {data["second_name"]}', code=data["code"], cid=data["id"], point=data["total_points"])
            team = Team.objects.get(cid=data["team"], code=data["team_code"])
            if not created:
                PlayerTeam.objects.get_or_create(player_id=player, team_id=team)
            else:
                PlayerTeam.objects.get_or_create(player_id=player, team_id=team)
            
        """ # Save the JSON data to a file
        with open("premiership.json", "w") as json_file:
            data = json.dump(json_data, json_file, indent=4)"""
            

        #print("JSON data saved to output.json")
    else:
        print(f"Error: {response.status_code}")
        
        
    
