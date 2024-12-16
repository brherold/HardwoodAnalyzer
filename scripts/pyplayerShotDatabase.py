import csv

#Adds Team Player Shots to playerShotDatabase.csv 

from pygameAnaylzer import gameAnaylzer
from pygameSearcher import gameSearcher

year = "2042"

def shotData_to_csv(playerDataShots):
    with open('playerShotDatabase' + year + '.csv', 'a', newline='') as csvfile:
        fieldnames = ['Player', 'PlayerID', 'F-M', 'F-A', 'F%', 'IS-M', 'IS-A', 'IS%', 'MR-M', 'MR-A', 'MR%', '3P-M', '3P-A', '3P%', 'DR-M', 'DR-A', 'DR%']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        for player in playerDataShots['players']:
            if player['shots']['Finishing'][1] != 0:
                finishing_percentage = player['shots']['Finishing'][0] / player['shots']['Finishing'][1]
            else:
                finishing_percentage = 0.0

            if player['shots']['Inside Shot'][1] != 0:
                inside_shot_percentage = player['shots']['Inside Shot'][0] / player['shots']['Inside Shot'][1]
            else:
                inside_shot_percentage = 0.0

            if player['shots']['Mid-Range'][1] != 0:
                mid_range_percentage = player['shots']['Mid-Range'][0] / player['shots']['Mid-Range'][1]
            else:
                mid_range_percentage = 0.0

            if player['shots']['3-Pointer'][1] != 0:
                three_pointer_percentage = player['shots']['3-Pointer'][0] / player['shots']['3-Pointer'][1]
            else:
                three_pointer_percentage = 0.0
            if player['driving'][1] != 0:
                driving_percentage = player['driving'][0] / player['driving'][1]
            else:
                driving_percentage = 0.0

            writer.writerow({
                'Player': player['name'],
                'PlayerID': player['playerCode'],
                'F-M': player['shots']['Finishing'][0],
                'F-A': player['shots']['Finishing'][1],
                'F%': '{:.2f}'.format(finishing_percentage),
                'IS-M': player['shots']['Inside Shot'][0],
                'IS-A': player['shots']['Inside Shot'][1],
                'IS%': '{:.2f}'.format(inside_shot_percentage),
                'MR-M': player['shots']['Mid-Range'][0],
                'MR-A': player['shots']['Mid-Range'][1],
                'MR%': '{:.2f}'.format(mid_range_percentage),
                '3P-M': player['shots']['3-Pointer'][0],
                '3P-A': player['shots']['3-Pointer'][1],
                '3P%': '{:.2f}'.format(three_pointer_percentage),
                'DR-M': player['driving'][0],
                'DR-A': player['driving'][1],
                'DR%': '{:.2f}'.format(driving_percentage)
            })

'''
#Creates the database"
with open('playerShotDatabase' + year + '.csv', 'w', newline='') as csvfile:
    fieldnames = ['Player', 'PlayerID', 'F-M', 'F-A', 'F%', 'IS-M', 'IS-A', 'IS%', 'MR-M', 'MR-A', 'MR%', '3P-M', '3P-A', '3P%', 'DR-M', 'DR-A', 'DR%']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
'''



#Adds teams from 1-430 (teamcode) into playerShotDatabaseYear.csv
errorTeams = [12,17,24,32,38,61,81,88,94,107,112,219,227,267,
              273,299,300,354,387,391,424,432,433,447,512,546,
              547,548,573,628,632,648,652,658,678,679,680,690,
              703,715,739,743,797,802,880,881,904,910,931,934,945,950.959,963,986,992]

for i in range(1,999):
    if i not in errorTeams:
        try:
            shotData_to_csv(gameSearcher(str(i), year, ""))
            print(i)
        except Exception as e:
            print(f"Error with team {i}: {e}")
            errorTeams.append(i)
            continue

print(errorTeams)
    


#shotData_to_csv(gameSearcher(str(999), year, ""))
