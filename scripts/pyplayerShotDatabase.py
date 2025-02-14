import csv

#Adds Team Player Shots to playerShotDatabase.csv 

from pygameAnalyzer import gameAnalyzer
from pygameSearcher import gameSearcher

year = "2043"

def shotData_to_csv(playerDataShots):
    with open('playerShotDatabase' + year + 'D.csv', 'a', newline='', encoding="utf-8") as csvfile:
        fieldnames = ['Player', 'PlayerID', 'F-M', 'F-A', 'F%', 'IS-M', 'IS-A', 'IS%', 
              'MR-M', 'MR-A', 'MR%', '3P-M', '3P-A', '3P%', 'OF-M', 'OF-A', 'OF%', 'OIS-M', 'OIS-A', 'OIS%', 
              'OMR-M', 'OMR-A', 'OMR%', 'O3P-M', 'O3P-A', 'O3P%']
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

            #defense
            if player['defense']['Finishing'][1] != 0:
                o_finishing_percentage = player['defense']['Finishing'][0] / player['defense']['Finishing'][1]
            else:
                o_finishing_percentage = 0.0

            if player['defense']['Inside Shot'][1] != 0:
                o_inside_shot_percentage = player['defense']['Inside Shot'][0] / player['defense']['Inside Shot'][1]
            else:
                o_inside_shot_percentage = 0.0

            if player['defense']['Mid-Range'][1] != 0:
                o_mid_range_percentage = player['defense']['Mid-Range'][0] / player['defense']['Mid-Range'][1]
            else:
                o_mid_range_percentage = 0.0

            if player['defense']['3-Pointer'][1] != 0:
                o_three_pointer_percentage = player['defense']['3-Pointer'][0] / player['defense']['3-Pointer'][1]
            else:
                o_three_pointer_percentage = 0.0


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

                'OF-M': player['defense']['Finishing'][0],
                'OF-A': player['defense']['Finishing'][1],
                'OF%': '{:.2f}'.format(o_finishing_percentage),
                'OIS-M': player['defense']['Inside Shot'][0],
                'OIS-A': player['defense']['Inside Shot'][1],
                'OIS%': '{:.2f}'.format(o_inside_shot_percentage),
                'OMR-M': player['defense']['Mid-Range'][0],
                'OMR-A': player['defense']['Mid-Range'][1],
                'OMR%': '{:.2f}'.format(o_mid_range_percentage),
                'O3P-M': player['defense']['3-Pointer'][0],
                'O3P-A': player['defense']['3-Pointer'][1],
                'O3P%': '{:.2f}'.format(o_three_pointer_percentage),

            })
            

'''
#Creates the database"
with open('playerShotDatabase' + year + 'D.csv', 'w', newline='') as csvfile:
    fieldnames = ['Player', 'PlayerID', 'F-M', 'F-A', 'F%', 'IS-M', 'IS-A', 'IS%', 
              'MR-M', 'MR-A', 'MR%', '3P-M', '3P-A', '3P%', 'OF-M', 'OF-A', 'OF%', 'OIS-M', 'OIS-A', 'OIS%', 
              'OMR-M', 'OMR-A', 'OMR%', 'O3P-M', 'O3P-A', 'O3P%']    
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
'''


#'''
#Adds teams from 1-430 (teamcode) into playerShotDatabaseYear.csv

#errorTeams = [8, 12, 17, 24, 32, 38, 61, 81, 88, 94, 95, 102, 107, 112, 146, 164, 195, 219, 227, 267, 269, 273, 292, 354, 365, 387, 391, 424, 432, 433, 447, 482, 507, 522, 546, 548, 573, 585, 622, 628, 646, 648, 652, 658, 674, 680, 686, 698, 703, 715, 739, 800, 811, 880, 881, 904, 910, 931, 938, 944, 945, 950, 963, 976, 986, 989]
'''
errorTeams =[]

for i in range(14,999):
    try:
        shotData_to_csv(gameSearcher(str(i), year, ""))
        print(i)
    except Exception as e:
        print(f"Error with team {i}: {e}")
        errorTeams.append(i)
        continue
    if i % 50 == 0:
        print()
        print(errorTeams)
        print()

print(errorTeams)
    

'''


shotData_to_csv(gameSearcher(str(867), year, ""))
#'''


