# ByBank Homework
# ---------------------------------------------------------------------------
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period
# Final script should both print the analysis to the terminal and export a text file with the results.

# ----------------------------------------------------
# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join(".","python-challenge","PythonChallenges","PyBank",'budget_data.csv')

# Method 2: Improved Reading using CSV module
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Go through file and add all the numbers in the second column, which is Net Profit and Losses of each month
    csv_header = next(csvreader)
    total = 0
    for row in csv.reader(csvfile):
        total += int(row[1])

with open(csvpath, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    data = list(reader)
    row_count = len(data)-1    

    
# -----------------------------------------------------------------------
# Print Summary
print("Financial Analysis")
print("------------------------")
print(f"Total Months: {str(row_count)}")
print(f"Total: ${str(total)}")
print("Average Change: $")
print(f"Greatest Increase in Profits: $")
print("Greatest Decrease in Profits: $")