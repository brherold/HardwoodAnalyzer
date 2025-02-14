#updated with player defense and uses playerCode instead of playername (useful for same name players)


from bs4 import BeautifulSoup
import requests


def gameAnalyzer(gameURL):

    page = requests.get(gameURL)
    soup = BeautifulSoup(page.text,"html")

    infoList = soup.find_all("td",class_="left")



    #'''
    gameData = {
    "awayTeam":{
        "name": infoList[1].text.replace("\xa0"," "),
        "teamCode":(infoList[1].find("a").get("href")).split("/")[2],
        "players":[],
        "totalShots":{"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0]},
        "defense" : {"man-to-man": {"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0], "Turnovers": [0, 0]},
                    "man-to-man defense packed" : {"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0], "Turnovers": [0, 0]},
                    "man-to-man defense extended" : {"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0], "Turnovers": [0, 0]},    
        "zone":{"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0], "Turnovers": [0, 0]},
        "zone defense packed":{"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0], "Turnovers": [0, 0]},
        "zone defense extended":{"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0], "Turnovers": [0, 0]},
        "pressure":{"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0], "Turnovers": [0, 0]},
        "transition": {"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0], "Turnovers": [0, 0]},
        "half-court": {"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0], "Turnovers": [0, 0]}}
    }
    ,
    "homeTeam":{
        "name": infoList[2].text.replace("\xa0"," "),
        "teamCode":(infoList[2].find("a").get("href")).split("/")[2],
        "players":[],
        "totalShots":{"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0]},
        "defense" : {"man-to-man": {"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0], "Turnovers": [0, 0]},
                    "man-to-man defense packed" : {"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0], "Turnovers": [0, 0]},
                    "man-to-man defense extended" : {"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0], "Turnovers": [0, 0]},    
        "zone":{"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0], "Turnovers": [0, 0]},
        "zone defense packed":{"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0], "Turnovers": [0, 0]},
        "zone defense extended":{"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0], "Turnovers": [0, 0]},
        "pressure":{"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0], "Turnovers": [0, 0]},
        "transition": {"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0], "Turnovers": [0, 0]},
        "half-court": {"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0], "Turnovers": [0, 0]}}
    }
    }


    curTeam = "awayTeam"
    infoListPlayers = infoList[4:]  # cuts it to the first player in BoxScore
    #print(infoList)
    for i in range(len(infoListPlayers)):
        #print(infoListPlayers[i])
        if len(infoListPlayers[i].text.split("\xa0")) == 3:
            #name, position = infoListPlayers[i].text.split("\xa0")[1:]
            name = " ".join(infoListPlayers[i].text.split("\xa0")[0:2])
            playerCode = infoListPlayers[i].find("a").get("href").split("/")[2]
            position = infoListPlayers[i].text.split("\xa0")[1:][-1]
            # Append a new player dictionary if the player index exceeds the current list length
            if len(gameData[curTeam]["players"]) <= i:
                gameData[curTeam]["players"].append({
                    "name": name, "position": position.upper(),
                    "playerCode": playerCode,
                    "shots": {"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0]}, 
                    "defense": {"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0]}, 
                    "stats":{"Min": 0, "FT": [0,0], "PTS": 0, "Reb": 0, "AST": 0, "STL": 0, "BLK": 0, "TO": 0, "PF": 0, "FD": 0 }})
            else:
                # Update existing player information
                gameData[curTeam]["players"][i]["name"] = name
                gameData[curTeam]["players"][i]["playerCode"] = playerCode
                gameData[curTeam]["players"][i]["position"] = position.upper()
                gameData[curTeam]["players"][i]["shots"] = {"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0]}
                gameData[curTeam]["players"][i]["defense"] = {"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0]}
                gameData[curTeam]["players"][i]["stats"] = {"Min": 0, "FT": [0,0], "PTS": 0, "Reb": 0, "AST": 0, "STL": 0, "BLK": 0, "TO": 0, "PF": 0, "FD": 0 }

            # Switch the team if the next player is "Total" and the current team is "homeTeam"
            if infoListPlayers[i + 1].text == "Total" and curTeam == "awayTeam":
                curTeam = "homeTeam"

    #Adds player box score stats 
    statsInfoArr = soup.find_all("table",class_="box-score")[-1].find_all("tr")[3:]
    findHomeTeam = []
    playerLines = []

    awayPlayerCount = 0
    for index, line in enumerate(statsInfoArr):
        if any(char.isalpha() for char in line.text):
            if statsInfoArr[index + 1].text and not statsInfoArr[index + 1].text[0].isdigit():
                break
            awayPlayerCount += 1

    for i in statsInfoArr:
        if i.text and i.text[0].isdigit():
            playerLines.append(i)


    curTeam = "awayTeam"
    for playerIndex, playerString in enumerate(playerLines):
        playerStatList = playerString.find_all("td")[3:]
        playerID = playerString.find("a").get("href").split("/")[-1]
        for player in gameData[curTeam]["players"]:
            if player["playerCode"] == playerID:
                
                player["stats"]["Min"] = int(playerStatList[0].text)
                player["stats"]["FT"][0] = int(playerStatList[3].text.split("-")[0])
                player["stats"]["FT"][1] = int(playerStatList[3].text.split("-")[1])
                player["stats"]["PTS"] = int(playerStatList[4].text)
                player["stats"]["Reb"] = int(playerStatList[6].text)
                player["stats"]["AST"] = int(playerStatList[7].text)
                player["stats"]["STL"] = int(playerStatList[8].text)
                player["stats"]["BLK"] = int(playerStatList[9].text)
                player["stats"]["TO"] = int(playerStatList[10].text)
                player["stats"]["PF"] = int(playerStatList[11].text)
                player["stats"]["FD"] = int(playerStatList[16].text)
                if playerIndex + 1 == awayPlayerCount:
                    curTeam = "homeTeam"
    
    #For getting box score logs
    playbyText = soup.find_all("div",id="Boxscore")[1].text
    gameArr = playbyText.split("\n")
    tipOff = gameArr[10]

    x = soup.find_all("div",id="Boxscore")[1]
    teamEventArr = x.find_all("b")[3:] #shows time and Team for each play-by-play Event (lined up with gameStartArr)

    #Lines up the events of gameEventsArr and teamEventArr
    gameEventsArr = gameArr[10:] # play-by-play Events
    for i in gameEventsArr:
        if i == "":
            gameEventsArr.remove(i)

    #Delete "Game Event","2nd Half","Overtime" and lines w/o ":" from gameEventsArr 
    gameEventsArr = [
    string for string in gameEventsArr
    if "Game Event" not in string
    and "2nd Half" not in string
    and "Overtime" not in string
    and ":" in string
]

    #Changes all Exclamations to Periods
    for i in range(len(gameEventsArr)):
        gameEventsArr[i] = gameEventsArr[i].replace("!",".")
    
    #Deletes time of play-by-play, Makes it easier to get the Offensive Team
    for i in range(len(gameEventsArr)):
        dash = "-"
        index = 0
        while(dash != gameEventsArr[i][index]):
            index += 1
        gameEventsArr[i] = gameEventsArr[i][index + 2:]

    
    # For splitting every shot attempt to a new line (including tip ins from missed shots)
    newGameEventsArr = []

    for event in gameEventsArr:
        if ("misses" in event or "blocks" in event or "blocked" in event) and ("tips it in") in event:
            words = event.split(":")

            team = words[0]
            sentence_event = event.split(". ")
            newGameEventsArr.append("".join(sentence_event[0:-3])) #before tip in
            newGameEventsArr.append(team + ": " + "".join(sentence_event[-3:])) #from tip in to end of string
            
        else:
            newGameEventsArr.append(event)
    
    #Delete Game Events with Non-And One Fouls (second free throws occur) and Charging Fouls
    gameEventsArr = [string for string in newGameEventsArr if "second free throw" not in string or "blocking out" in string or  ("second free throw" in string and "shot goes in" in string)]
    gameEventsArr = [string for string in newGameEventsArr if "charged with the foul" not in string]

    #Holds shot types and turnover phrases
    shotTypes = {    
        "Inside Shot": ["shoots from the inside","shoots from the low post", "shoots in the paint", "shoots from inside the arc", "shoots from the block","tips it in","attempts to dunk it" , "lays it up", "goes for the dunk"],
        "Mid-Range": ["with a fadeaway jumper","shoots a jumper"],
        "3-Pointer": ["shoots from beyond the arc","shoots from well beyond the arc","shoots from the three point line", "shoots from deep" , "shoots from the corner","shoots from downtown"]
    }

    Finishing = {"attempts to dunk it" , "lays it up", "goes for the dunk"}

    Turnover = {"turns the ball over", "steals the pass"}
    
    fg_attempts = {"shot goes in", "Slam dunk", "tips it in", "shot misses", "blocks the shot", "blocked", "Air ball"}

    missed_attempts = {"shot misses", "blocks the shot", "blocked", "Air ball"} #missed shots

    made_attempts = {"shot goes in", "Slam dunk", "tips it"}

    turnover_phrases = {"steals the pass", "turns the ball over", "on the shot."}


    #From Script game logs to get full playerName and defender name
    
    #playerName:playerCode
    player_dic = {} #matches playerCode with playerName (use to match when going through shots to determine which player is which (for players with same last name))

    textArr = []
    for index in soup.find_all("script"):
        if "myFunction" in index.text:
            textArr.append(index.text)
      
    shotTextArr = []

    for text in textArr:
        splitted = text.split("\\")
        name = splitted[10].replace(">","<").split("<")[1]
        id_text = text.split(" ")[17][12:-2] #gets ID of team or player

        if len(id_text) > 5:
            playerCode = id_text
            player_dic[name] = playerCode
            #thats playerID
        if len(id_text) < 5:
            shotTextArr.append(text)

    shotTextArr[0].split("\\")

    shotArr = []
    curTeam = "awayTeam"
    away_shots = []
    home_shots = []
    total_team_shots = {"awayTeam": [], "homeTeam": []}

    for i in range(len(shotTextArr)):
        arr = shotTextArr[i].split("\\")
        for text in arr:
            if "shot clock" in text:

                shot_parsedArr = text.replace(":  ", " [").split(" [")
                offense_player = shot_parsedArr[1].split(" - ")[0] #gets offensive player for shot 
                defense_player = shot_parsedArr[1].split(" by ")[-1]
                total_team_shots[curTeam].append((offense_player,defense_player))

        curTeam = "homeTeam"

        #shotsTextArr = shotArr[::2]

    total_team_shots["awayTeam"] = total_team_shots["awayTeam"][::2]
    total_team_shots["homeTeam"] = total_team_shots["homeTeam"][::2]

    awayTeamEventCounter = -1 #starts at -1 so initial gets event gets incremented (align with gamelog shot events)
    homeTeamEventCounter = -1

    #Scrapes gamelog and matches it with total_team_shots
    #shot_attempt 0 -> missed 1 -> made
    for i, event in enumerate(gameEventsArr):
        team = event.split(":")[0]
        #Find team 
        if team in gameData["homeTeam"]["name"]:
            team = "homeTeam"
            oppTeam = "awayTeam"  
        else:
            team = "awayTeam"
            oppTeam = "homeTeam"
        
        #Find type of defense being played
        try:
            defense = [defense for defense in gameData["awayTeam"]["defense"] if defense in event][-1]
        
        except IndexError:
            defense = "half-court"
        
        if any(phrase in event for phrase in fg_attempts):
            for shot_type, shots in shotTypes.items():

                for shot in shots:
                    shot_attempt = 0
                    if shot in event:

                        if ("Breakaway" in event or "Fast break opportunity" in event) and "slow it down" not in event:
                            defense = "transition"
                            if shot in Finishing:
                                shot_type = "Finishing"

                        #For Drives
                        if shot in Finishing and "drives" in event:
                            #Find who drove and whether that player shot it
                            split_event = event.split(". ")
                            drive_index = next(i for i, s in enumerate(split_event) if "drives" in s)
                            shot_index = next(i for i, s in enumerate(split_event) if shot in s)
                            if shot_index == drive_index + 1:
                                shot_type = "Finishing"

                        #finds player and accumlates the shot in gameData
                        if team == "awayTeam":
                            awayTeamEventCounter += 1
                            shot_event = total_team_shots["awayTeam"][awayTeamEventCounter]
                        else:
                            homeTeamEventCounter += 1
                            shot_event = total_team_shots["homeTeam"][homeTeamEventCounter]


                        #Finds the offensive and defensive playerCode
                        offense_playerCode = player_dic[shot_event[0]]
            
                        try:
                            defense_playerCode = player_dic[shot_event[1]]
                        except: 
                            defense_playerCode = None #if shot had no defenders (tip in)

                        #determines if player made or missed the shot  
                        if any(phrase in event for phrase in missed_attempts):  
                            shot_attempt = 0
                        elif any(phrase in event for phrase in made_attempts): 
                            shot_attempt = 1
                            #For Fast-breaks


                        
                        
                        for player in gameData[team]["players"]:     
                            
                            if offense_playerCode == player["playerCode"]:
                                
                                player["shots"][shot_type][0] += shot_attempt
                                player["shots"][shot_type][1] += 1
                                gameData[team]["totalShots"][shot_type][0] += shot_attempt
                                gameData[team]["totalShots"][shot_type][1] += 1

                                gameData[oppTeam]["defense"][defense][shot_type][0] += shot_attempt
                                gameData[oppTeam]["defense"][defense][shot_type][1] += 1

                                gameData[oppTeam]["defense"][defense]["Turnovers"][1] += 1 #Defense event counter [forced turnovers,defensive events occured]
                        
                        for player in gameData[oppTeam]["players"]:
                            
                            if defense_playerCode and defense_playerCode == player["playerCode"]:
                                
                                player["defense"][shot_type][0] += shot_attempt
                                player["defense"][shot_type][1] += 1


            
        else:
            if any(phrase in event for phrase in turnover_phrases):
                #Adds turnovers in defense (not offensive fouls)
                gameData[oppTeam]["defense"][defense]["Turnovers"][0] += 1
                gameData[oppTeam]["defense"][defense]["Turnovers"][1] += 1 #Defense event counter [forced turnovers,defensive events occured]



    #used for getting GAME CODE and GAME TYPE
    soup2 = soup 

    date = soup2.find("div",{"id": "Main"}).find_all("h3")[0]
    type_id = soup2.find("div",{"id": "Main"}).find_all("h3")[1]

    first_half_months = ["October","November","December"]

    date_split = date.text[7:].replace(",","").split(" ")

    month = date_split[0]
    year = int(date_split[-1])

    if month in first_half_months:
        season = year + 1
    else:
        season = year




    game_type_unparsed = type_id.text[15:].split(" ")[0]
    game_id_unparsed = type_id.text[15:].split(" ")[-2]

    game_type = game_type_unparsed.strip("[]")

    game_id = int(game_id_unparsed.strip("[]#"))

    gameData["season_year"] = season
    gameData["game_id"] = game_id
    gameData["game_type"] = game_type

    return gameData

#print(gameAnalyzer("http://onlinecollegebasketball.org/game/1027313"))