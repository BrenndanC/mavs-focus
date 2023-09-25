import http.client, json, time, config

# Sets connection to correct API
conn = http.client.HTTPSConnection("api.sportradar.us")

# Requests team profile for the Dallas Mavericks
conn.request("GET", "/nba/trial/v8/en/teams/" + config.MAVS_ID + "/profile.json?api_key=" + config.API_KEY)

# Reads the response from the API
res = conn.getresponse()
data = res.read()

# Loads the data into a json object
team_data = json.loads(data)

def player_stats(player_id):
    conn = http.client.HTTPSConnection("api.sportradar.us")
    conn.request("GET", "/nba/trial/v8/en/players/" + player_id + "/profile.json?api_key=" + config.API_KEY)
    res = conn.getresponse()
    data = res.read()
    player_stats = json.loads(data)
    return player_stats

# print(data.decode("utf-8"))
for player in team_data['players']:
        print(player['full_name'])
        time.sleep(1)
        stats = player_stats(player['id'])
        for season in stats['seasons']:
            year = season['year']
            teams = season['teams']
            # Will handle if player has only played on one team that season
            if len(teams) == 1:
                alias = teams[0]['alias']
                averages = teams[0]['average']
                points = averages['points']
                rebounds = averages['rebounds']
                assists = averages['assists']
            # Handles the case where the player has played on multiple teams that season
            else:
                alias = ""
                totPts = 0
                totReb = 0
                totAst = 0
                totGames = 0
                for team in teams:
                    if alias == "":
                        alias = team['alias']
                    else:
                        alias = alias + "/" + team['alias']
                    totPts += team['total']['points']
                    totReb += team['total']['rebounds']
                    totAst += team['total']['assists']
                    totGames += team['total']['games_played']
                points = totPts/totGames
                rebounds = totReb/totGames
                assists = totReb/totGames
            print("     " + str(year) + " [" + alias + "]:")
            print("          " + str(points), "PPG")
            print("          " + str(rebounds), "REB")
            print("          " + str(assists), "AST")
        

