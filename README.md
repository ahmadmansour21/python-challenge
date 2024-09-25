# python-challenge
In this challenge, we are tasked with developing code to acquire data from two csv files, generating an analysis of these files. In the first portion - PyBank - the analysis is meant to include calculations of: 

The total number of months included in the dataset - done so using a for loop that passes through each row in the csv dataset. In the code total_months = total_months + 1, the calculation of total months is stored in the variable total_months and what it does is utilize the for loop to keep adding an additional month into this calculation until the final row of months.

The net total amount of "Profit/Losses" over the entire period - done so using total_net = total_net + int(row[1]) which uses the same for loop to add up all of the profit/losses values in the second column (int(row[1])) to to each other to calculate how much net change occurred over the whole period.

The changes in "Profit/Losses" over the entire period, and then the average of those changes - done so using change = int(row[1]) - previous_value
        previous_value = int(row[1])
        sum_of_changes = change + sum_of_changes - which uses the same for loop to add up the profit/losses value in the subsequent row (int(row[1])) in the second column to the previous row (previous_value) to calculate how much change occurred in profit/losses per month (change), over the whole period (sum_of_changes).

The greatest increase in profits (date and amount) over the entire period - done so using 
if change > greatest_increase:
            greatest_month = row[0]
            greatest_increase = change - this if statement is ensuring that if the row that the loop is currently in displays a change value that is the maximum, then store that into greatest_increase and the month associated with it (row[0]) into greatest_month. As the loop goes, it will continuously replace that greatest_increase value so long as the change in the subsequent row is higher than the previous one.

The greatest decrease in profits (date and amount) over the entire period - same logic as the previous point but with lowest change and done so using - if change < greatest_decrease:
            lowest_month = row[0]
            greatest_decrease = change 

The python file for this code can be found in the "PyPBank" folder within my python-challenge repository and the text file with the output can be found in the "Analysis" folder within the "PyBank" folder.

In the second portion - PyPoll - we are tasked with finding:

The total number of votes cast - same logic as total_months in PyBank, done so using 
total_votes = total_votes + 1


A complete list of candidates who received votes

The percentage of votes each candidate won

The total number of votes each candidate won

For the 3 prompts above, the logic is as follows: a dictionary was created with the candidate names and total votes associated with each name using: 
if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1 - this code essentially ensures that candidate names will be stored into the variable candidate and the for loop will go through each row in the csv file to display each candidate name once in the dictionary. The if statement says if the candidate name already appears in the dictionary then add a vote to the vote count associated with that name (candidate_votes[candidate] += 1). If not, then this must be a new name (next candidate) seeing as it does not already appear in the dictionary and therefore add 1 vote to that name (else: candidate_votes[candidate] = 1). Once this is done, we go back to the if statement for this new candidate, adding votes to this already existing candidate until the next candidate name is reached in the csv file at which point we go to the else statement again to add this new candidate and the votes associated.

            Once done, we use this code to calculate the percentages associated with these votes per candidate: 
for candidate, votes in candidate_votes.items()
        candidate_percentages[candidate] = (votes / total_votes) * 100.

The winner of the election based on popular vote
To get the winner, same logic is used as for greatest_increase in PyBank, done so using this code: 
if votes > winning_votes:
            winner = candidate
            winning_votes = votes

The python file for this code can be found in the "PyPoll" folder within my python-challenge repository and the text file with the output can be found in the "Analysis" folder within the "PyPoll" folder.

Xpert Learning Tool was used in moments of errors and uncertainety to help me code and generate the correct output.