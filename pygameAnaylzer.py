from bs4 import BeautifulSoup
import requests
#USE PYTHON ANACADONA 3.8.5 to RUN

def gameAnaylzer(gameUrl):
  #url= "http://onlinecollegebasketball.org/game/856168"
  page = requests.get(gameUrl)
  soup = BeautifulSoup(page.text,"html")

  infoList = soup.find_all("td",class_="left")
  infoList = soup.find_all("td",class_="left")
  gameData = {
  "awayTeam":{
    "name": infoList[1].text.replace("\xa0"," "),
    "teamCode":(infoList[1].find("a").get("href")).split("/")[2],
    "players":[],
    "totalShots":{"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0]},
    "totalDriving":[0,0],
    "defense" : {"man-to-man": {"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0]},
    "zone":{"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0]},
    "pressure":{"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0]},
    "transition": {"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0]}}
  }
  ,
  "homeTeam":{
    "name": infoList[2].text.replace("\xa0"," "),
    "teamCode":(infoList[2].find("a").get("href")).split("/")[2],
    "players":[],
    "totalShots":{"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0]},
    "totalDriving":[0,0],
    "defense" : {"man-to-man": {"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0]},
    "zone":{"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0]},
    "pressure":{"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0]},
    "transition": {"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0]}}
  }
}



  teamSwitch = 0 
  curTeam = "awayTeam"
  infoListPlayers = infoList[4:]  # cuts it to the first player in BoxScore

  for i in range(len(infoListPlayers)):
      if len(infoListPlayers[i].text.split("\xa0")) == 3:
          name, position = infoListPlayers[i].text.split("\xa0")[1:]
          
          # Append a new player dictionary if the player index exceeds the current list length
          if len(gameData[curTeam]["players"]) <= i:
              gameData[curTeam]["players"].append({"name": name, "position": position.upper(), "shots": {"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0]}, "driving": [0, 0]})
          else:
              # Update existing player information
              gameData[curTeam]["players"][i]["name"] = name
              gameData[curTeam]["players"][i]["position"] = position.upper()
              gameData[curTeam]["players"][i]["shots"] = {"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0]}
              gameData[curTeam]["players"][i]["driving"] = [0, 0]

          # Switch the team if the next player is "Total" and the current team is "homeTeam"
          if infoListPlayers[i + 1].text == "Total" and curTeam == "awayTeam":
              curTeam = "homeTeam"

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
  #Changes all Exclamations to Periods
  for i in range(len(gameEventsArr)):
    gameEventsArr[i] = gameEventsArr[i].replace("!",".")
  gameEventsArr = gameEventsArr[:-1]
  #Delete "Game Event","2nd Half","Overtime" and lines w/o ":" from gameEventsArr 

  gameEventsArr = [
    string for string in gameEventsArr
    if "Game Event" not in string
    and "2nd Half" not in string
    and "Overtime" not in string
    and ":" in string
]
  #Deletes time of play-by-play, Makes it easier to get the Offensive Team


  for i in range(len(gameEventsArr)):
    dash = "-"
    index = 0
    while(dash != gameEventsArr[i][index]):
        index += 1
    gameEventsArr[i] = gameEventsArr[i][index + 2:]
  #Determines whether a drive is successful or not
  Driving = {
    "Fail":"drive ",
    "Success":"drives "
  }

  #Driving["Fail"] in event
  #Adds all the drivers
  drive_attempt = -1 #-1: No Drive, 0: Fail, 1: Success
  for event in gameEventsArr:
    if Driving["Fail"] in event or Driving["Success"] in event:
      drive_attempt = 0
      if Driving["Success"] in event:
        drive_attempt = 1
      words = event.split()
      team = words[0][:-1] #team of driver
      if drive_attempt == 0:
        drive_index = words.index("drive")
        player_index = drive_index - 3
      else:
        drive_index = words.index("drives")
        player_index = drive_index - 1
      player_name = words[player_index] #driver name

      
      if team in gameData["homeTeam"]["name"]:
        team = "homeTeam"
      else:
        team = "awayTeam"
      for player in gameData[team]["players"]:
        if player["name"] == player_name:
          player["driving"][0] += drive_attempt
          player["driving"][1] += 1
          gameData[team]["totalDriving"][0] += drive_attempt
          gameData[team]["totalDriving"][1] += 1


  #Delete Game Events with Non-And One Fouls (second free throws occur) and Charging Fouls
  gameEventsArr = [string for string in gameEventsArr if "second free throw" not in string or "blocking out" in string]
  gameEventsArr = [string for string in gameEventsArr if "charged with the foul" not in string]

  shotTypes = {    
      "Inside Shot": ["shoots from the inside","shoots from the low post", "shoots in the paint", "shoots from inside the arc", "shoots from the block","tips it in","attempts to dunk it" , "lays it up", "goes for the dunk"],
      "Mid-Range": ["with a fadeaway jumper","shoots a jumper"],
      "3-Pointer": ["shoots from beyond the arc","shoots from well beyond the arc","shoots from the three point line", "shoots from deep" , "shoots from the corner","shoots from downtown"]
  }

  Finishing = {"attempts to dunk it" , "lays it up", "goes for the dunk"}


  #Adds every FG into the gameData per Player
  for event in gameEventsArr:
    for shot_type, shots in shotTypes.items():
      for shot in shots:
        shot_attempt = 0
        if shot in event:
          words = event.split()
          player_index = words.index(shot.split()[0]) - 1
          player_name = words[player_index]
          team = words[0][:-1]

            #Finds the type of defense (doesn't matter for gameData["team"])
          try:
            defense = [defense for defense in gameData["awayTeam"]["defense"] if defense in event][0]
          except IndexError:
            defense = "no defense"

          if "Slam dunk" in event or "shot goes in" in event or "tips it in" == shot:
            shot_attempt = 1
          
          #For Fast-breaks

          if ("Breakaway" in event or "Fast break opportunity" in event) and "slow it down" not in event:
            defense = "transition"
            if shot in Finishing:
              shot_type = "Finishing"

          #For Drives
          if shot in Finishing and "drives" in event and words[words.index("drives") - 1] == player_name:
            shot_type = "Finishing"

          #finds player and accumlates the shot in gameData
          if team in gameData["homeTeam"]["name"]:
            team = "homeTeam"
            oppTeam = "awayTeam"
          else:
            team = "awayTeam"
            oppTeam = "homeTeam"

          for player in gameData[team]["players"]:
            if player["name"] == player_name:
              player["shots"][shot_type][0] += shot_attempt
              player["shots"][shot_type][1] += 1
              gameData[team]["totalShots"][shot_type][0] += shot_attempt
              gameData[team]["totalShots"][shot_type][1] += 1

              if defense != "no defense":
                gameData[oppTeam]["defense"][defense][shot_type][0] += shot_attempt
                gameData[oppTeam]["defense"][defense][shot_type][1] += 1

  return gameData
