# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("/Users/ahmedmansour/Desktop/datacourse/python-challenge/PyPoll/Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("/Users/ahmedmansour/Desktop/datacourse/python-challenge/PyPoll/analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
candidate_votes = {}
candidate_percentages = {}
winner = str
winning_votes = 0

# Define lists and dictionaries to track candidate names and vote counts

# Winning Candidate and Winning Count Tracker

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
       #print(". ", end="")

        # Increment the total vote count for each row
        total_votes = total_votes + 1

        # Get the candidate's name from the row
        candidate = row[2]

        #  If the candidate is not already in the candidate list, add them
        

        # Add a vote to the candidate's count
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
        

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print("Election Results")
    print("--------------------------")
    print("Total Votes:", total_votes)
    print("--------------------------")
    

    # Write the total vote count to the text file
    final_output = ("Election Results\n"
    "--------------------------\n"
    f"Total Votes: {total_votes}\n"
    "--------------------------\n")

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate, votes in candidate_votes.items():

        # Get the vote count and calculate the percentage
    
        candidate_percentages[candidate] = (votes / total_votes) * 100

        # Update the winning candidate if this one has more votes
        if votes > winning_votes:
            winner = candidate
            winning_votes = votes

        # Print and save each candidate's vote count and percentage
        print(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({votes})")
       
        output0 = (f"{candidate}: {candidate_percentages[candidate]:.3f}% ({votes})\n")
        final_output = final_output + output0

    # Generate and print the winning candidate summary
print("--------------------------")
print("Winner:", winner)
print("--------------------------")

output_1 = ("--------------------------\n"
f"Winner: {winner}\n"
"--------------------------\n")
    # Save the winning candidate summary to the text file
final_output = final_output + output_1

with open(file_to_output, "w") as txt_file:
  txt_file.write(final_output)
