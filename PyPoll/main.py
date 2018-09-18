import os

# Module for reading CSV files

import csv

file_to_read = os.path.join( "Resources", "election_data.csv")
file_to_write = os.path.join( "Analysis", "election_analysis.txt")

with open(file_to_read, newline='') as csvfile:

# CSV reader specifies delimiter and variable that holds contents

    csvreader = csv.reader(csvfile, delimiter=',')

    has_header = csv.Sniffer().has_header(csvfile.read(1024))
    csvfile.seek(0)  
    reader = csv.reader(csvfile)
    if has_header:
        next(reader)
    election_data_list = list(csvreader)

# total number of rows in raw data as each record is a polled vote

total_votes = len(election_data_list)

unique_candidates_list = []

# get unique candidates list

for x in election_data_list:
    if x[2] not in unique_candidates_list:
       unique_candidates_list.append(x[2]) 

# get polled votes for each candiate in unique candidate list

polled_votes = []
counter = 0
for y in range(len(unique_candidates_list)):
    for i in range(len(election_data_list)):
        if election_data_list[i][2] == unique_candidates_list[y]:
            counter += 1
    polled_votes.append([unique_candidates_list[y],counter,"{0:.3f}%".format(counter*100/total_votes)])
    counter = 0

# winner based on maximum polled votes

winner = max(polled_votes, key=lambda x: x[1])         


print(f"\nElection Results" \
      f"\n--------------------------" \
      f"\nTotal Votes:{total_votes} " \
      f"\n---------------------------\n" , end = "")

for i in range(len(polled_votes)):
    print(f"{polled_votes[i][0]}: {polled_votes[i][2]} ({polled_votes[i][1]})")

print(f"\n--------------------------" \
      f"\nWinner: {winner[0]} " \
      f"\n--------------------------\n", end = "")

# write to text file

with open( file_to_write, "w") as text_file:
          print(f"\nElection Results" \
                f"\n--------------------------" \
                f"\nTotal Votes:{total_votes} " \
                f"\n---------------------------\n" , end = "", file = text_file)

          for i in range(len(polled_votes)):
              print(f"{polled_votes[i][0]}: {polled_votes[i][2]} ({polled_votes[i][1]})", file = text_file) 

          print(f"\n--------------------------" \
                f"\nWinner: {winner[0]} " \
                f"\n--------------------------\n", end = "" , file = text_file)
        





    

 