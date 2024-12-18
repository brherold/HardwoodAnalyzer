from pygameSearcher import gameSearcher
import os


    
'''
total_defense_dic = {
    "defense" : {"man-to-man": {"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0]},
                 "man-to-man defense packed" : {"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0]},
                 "man-to-man defense extended" : {"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0]},    
    "zone":{"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0]},
    "zone defense packed":{"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0]},
    "zone defense extended":{"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0]},
    "pressure":{"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0]},
    "transition": {"Finishing": [0, 0], "Inside Shot": [0, 0], "Mid-Range": [0, 0], "3-Pointer": [0, 0]}}}
'''


total_defense_dic = {}
file_path = "total_defense_dic.txt"

try:
    with open(file_path, "r") as file:
        total_defense_dic = eval(file.read())
except:
    print("Error")




for teamCode in range(100,200):
    year = "2042"
    try:
        curr_dic = gameSearcher(str(teamCode),year,"")
        curr_dic_def = curr_dic["defense"]
        for def_type in curr_dic_def:
            for shot_type in curr_dic_def[def_type]:
                total_defense_dic["defense"][def_type][shot_type][0] += curr_dic_def[def_type][shot_type][0]
                total_defense_dic["defense"][def_type][shot_type][1] += curr_dic_def[def_type][shot_type][1]
        print(teamCode)
    except:
        print("Error " + str(teamCode)) 
    


print(total_defense_dic)

#save_html_to_file(total_defense_dic, "total_defense_dic.txt")