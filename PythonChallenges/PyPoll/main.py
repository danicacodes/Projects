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

# Create Lists
total_votes = []
candidates = []
percent_won_votes = []
total_won_votes = []
winner = []

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Go through file and add total votes
    csv_header = next(csvreader)
    for row in csv.reader(csvfile):
        total_votes.append(row[0])


# Print Election Results
print("Election Results")
print("-----------------------------------------")
print(f"Total Votes: {len(total_votes)}")
print("-----------------------------------------")
print("Kan: ")
print("Correy: ")
print("Li: ")
print("O'Tooley: ")
print("-----------------------------------------")
print("Winner: ")
print("-----------------------------------------")