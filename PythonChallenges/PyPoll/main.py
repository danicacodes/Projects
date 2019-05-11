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
    percent_khan = (khan_votes/total_votes)
    percent_correy = (correy_votes/total_votes)
    percent_li = (li_votes/total_votes)
    percent_otooley = (otooley_votes/total_votes)

    candidate_results = [khan_votes, correy_votes, li_votes, otooley_votes]
    winner = max(candidate_results)

    if winner == khan_votes:
        winner_name = "Khan"
    elif winner == correy_votes:
        winner_name = "Correy"
    elif winner == li_votes:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley"

# Print Election Results
print("Election Results")
print("-----------------------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------------------")
print(f"Khan: {percent_khan:.3%} {khan_votes}")
print(f"Correy: {percent_correy:.3%} {correy_votes}")
print(f"Li: {percent_li:.3%}% {li_votes}")
print(f"O'Tooley: {percent_otooley:.3%}% {otooley_votes}")
print("-----------------------------------------")
print(f"Winner: {winner_name} with {winner} votes")
print("-----------------------------------------")

# -----------------------------------------------------------------------
# Specify the file to write to
# output_path = os.path.join(".","python-challenge","PythonChallenges","PyPoll",'ElectionResults.csv')

# Open the file using "write" mode. Specify the variable to hold the contents
with open('python-challenge\PythonChallenges\PyPoll\ElectionResults.txt','w') as outfile:
    
    # Initiate csv.writer
    # csvwriter = csv.writer(csvfile, delimiter=',')

    #Write first row - Election Results
    print(["Election Results"], file=outfile)
    print(['----------------------------'], file=outfile)
    
    # Write Total Votes
    print([f"Total Votes: {total_votes}"], file=outfile)
    print(['----------------------------'], file=outfile)
    
    #Write Candidate Results
    print([f"Khan: {percent_khan:.3%} ({khan_votes})"], file=outfile)
    print([f"Correy: {percent_correy:.3%} ({correy_votes})"], file=outfile)
    print([f"Li: {percent_li:.3%} ({li_votes})"], file=outfile)
    print([f"O'Tooley: {percent_otooley:.3%} ({otooley_votes})"], file=outfile)
    print(['----------------------------'], file=outfile)

    #Write Winner
    print([f"Winner: {winner_name} with {winner} votes"], file=outfile)
    print(['----------------------------'], file=outfile)