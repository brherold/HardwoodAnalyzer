#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import os
from pygameAnaylzer import gameAnaylzer



#USE PYTHON ANACADONA 3.8.5 to RUN


# In[2]:
#Saves HTML Content to local File
def save_html_to_file(content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

# Function to load HTML content from a local file
def load_html_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

#Gets Team
#teamCode = input("Enter Team Code")
#year = input("Enter Season Year")
def gameSearcher(teamCode,year):

  teamScheduleUrl = "http://onlinecollegebasketball.org/schedule/"+teamCode + "/" + year
  
  cache_folder = "TeamsHTML"
  cache_filename = os.path.join(cache_folder, f"{teamCode}_{year}.html")
  try:
        # Try to load HTML content from the local cache
        html_content = load_html_from_file(cache_filename)
        #print("Content loaded from local cache.")
  except FileNotFoundError:
        # If not found, fetch the content from the URL
        response = requests.get(teamScheduleUrl)
        html_content = response.text

        # Save HTML content to the local cache
        save_html_to_file(html_content, cache_filename)
        #print("Content fetched from URL and saved to local cache.")

  #page2 = requests.get(teamScheduleUrl)
  #soup2 = BeautifulSoup(page2.text,"html")
  soup2 = BeautifulSoup(html_content,"html")


  # In[3]:


  #Gets List of All Played Games for Current Year
  columnList = soup2.find_all("tr")
  totalGameLinks = []
  for row in columnList:
    rowData = row.find_all("td")
    if len(rowData) == 8 and rowData[5].text != "NPY":
      totalGameLinks.append ("http://onlinecollegebasketball.org" + rowData[5].find("a").get("href"))

  conGameLinks = totalGameLinks[13:43] #Conference Games
  #test = conGameLinks[0:2]


  # In[4]:


  anaylzedGames = []
  for games in conGameLinks:
    anaylzedGames.append(gameAnaylzer(games)) 

  #Puts together Game Data for the Given Team for Every Game Played
  teamTotalData = []
  for games in anaylzedGames:
    if games['awayTeam']['teamCode'] == teamCode:
      teamTotalData.append(games['awayTeam'])
    else: 
      teamTotalData.append(games['homeTeam'])


  # In[ ]:


  #Calculates Total Season Stats
  fullPlayerStats = teamTotalData[0]

  for data in teamTotalData:
    if data != fullPlayerStats:
      #Now check if a player's name in data is in FullPlayerStats
      for dataPlayer in data["players"]:
        dataPlayerName = dataPlayer["name"]
        if not any(player['name'] == dataPlayerName for player in fullPlayerStats['players']): #If player isn't found in fullPlayerStats add it 
          fullPlayerStats["players"].append(dataPlayer)
        else:
          for index, player in enumerate(fullPlayerStats["players"]): # finds index of player in fullPlayerStats
            if player["name"] == dataPlayerName:
              fullPlayerStats["players"][index]["driving"][0] += dataPlayer["driving"][0]
              fullPlayerStats["players"][index]["driving"][1] += dataPlayer["driving"][1]
              fullPlayerStats["totalDriving"][0] += dataPlayer["driving"][0]
              fullPlayerStats["totalDriving"][1] += dataPlayer["driving"][1]

              for shot_type in fullPlayerStats["players"][index]["shots"]:
                fullPlayerStats["players"][index]["shots"][shot_type][0] += dataPlayer["shots"][shot_type][0]
                fullPlayerStats["players"][index]["shots"][shot_type][1] += dataPlayer["shots"][shot_type][1]
                fullPlayerStats["totalShots"][shot_type][0] += dataPlayer["shots"][shot_type][0]
                fullPlayerStats["totalShots"][shot_type][1] += dataPlayer["shots"][shot_type][1]

      
      
      for defense in data["defense"]:
        for defendedShot in data["defense"][defense]:
          fullPlayerStats["defense"][defense][defendedShot][0] += data["defense"][defense][defendedShot][0]
          fullPlayerStats["defense"][defense][defendedShot][1] += data["defense"][defense][defendedShot][1]

    

      

  return fullPlayerStats
            
    
        
        
#print(gameSearcher("533","2036"))


