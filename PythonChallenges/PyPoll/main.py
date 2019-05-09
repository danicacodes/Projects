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

    # Count votes per candidate
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

    # Percent of votes per candidate
    percent_khan = (khan_votes/total_votes)*100
    percent_correy = (correy_votes/total_votes)*100
    percent_li = (li_votes/total_votes)*100
    percent_otooley = (otooley_votes/total_votes)*100

    candidate_results = [khan_votes, correy_votes, li_votes, otooley_votes]
    winner = max(candidate_results)

# Print Election Results
print("Election Results")
print("-----------------------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------------------")
print(f"Khan: {(round(percent_khan))}% {khan_votes}")
print(f"Correy: {(round(percent_correy))}% {correy_votes}")
print(f"Li: {(round(percent_li))}% {li_votes}")
print(f"O'Tooley: {(round(percent_otooley))}% {otooley_votes}")
print("-----------------------------------------")
print(f"Winner: Khan with {khan_votes} votes")
print("-----------------------------------------")

# -----------------------------------------------------------------------
# Specify the file to write to
output_path = os.path.join(".","python-challenge","PythonChallenges","PyPoll",'ElectionResults.csv')

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path,'w', newline='') as csvfile:
    
    # Initiate csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    #Write first row - Election Results
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(['----------------------------'])
    
    # Write Total Votes
    csvwriter.writerow([f"Total Votes: {total_votes}"])
    csvwriter.writerow(['----------------------------'])
    
    #Write Candidate Results
    csvwriter.writerow([f"Khan: {(round(percent_khan))}% ({khan_votes})"])
    csvwriter.writerow([f"Correy: {(round(percent_correy))}% ({correy_votes})"])
    csvwriter.writerow([f"Li: {(round(percent_li))}% ({li_votes})"])
    csvwriter.writerow([f"O'Tooley: {(round(percent_otooley))}% ({otooley_votes})"])
    csvwriter.writerow(['----------------------------'])

    #Write Winner
    csvwriter.writerow([f"Winner: Khan with {khan_votes} votes"])
    csvwriter.writerow(['----------------------------'])