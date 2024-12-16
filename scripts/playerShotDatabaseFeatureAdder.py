#Adds the features to an already made and data-filled playerShotDatabase.py 



import csv

# Define the new field names
fieldnames = ['Player', 'PlayerID', 'F-M', 'F-A', 'F%', 'IS-M', 'IS-A', 'IS%', 
              'MR-M', 'MR-A', 'MR%', '3P-M', '3P-A', '3P%', 'DR-M', 'DR-A', 'DR%']


playerShotDatabase = 'playerShotDatabase'
def CSVfeatureAdder(playerShotDatabase):
# Read the original data
  with open(playerShotDatabase, 'r') as infile:
      reader = csv.reader(infile)
      original_data = list(reader)

  # Write the new header and the original data to a new file
  with open(playerShotDatabase, 'w', newline='') as outfile:
      writer = csv.writer(outfile)
      writer.writerow(fieldnames)  # Write the header
      writer.writerows(original_data)  # Write the original data


CSVfeatureAdder('playerShotDatabase2042.csv')