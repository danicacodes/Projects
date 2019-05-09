# PyPoll Homework
# ------------------------------------------------
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.
# ------------------------------------------------
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join(".","python-challenge","PythonChallenges","PyPoll",'election_data.csv')

# Create all variables
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #Skip the header
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes +=1
        if row[2] == "Khan":
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li":
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1


# Print Election Results
print("Election Results")
print("-----------------------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------------------")
print("Kan: ")
print("Correy: ")
print("Li: ")
print("O'Tooley: ")
print("-----------------------------------------")
print("Winner: ")
print("-----------------------------------------")