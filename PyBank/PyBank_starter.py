# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("/Users/ahmedmansour/Desktop/datacourse/python-challenge/PyBank/Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("/Users/ahmedmansour/Desktop/datacourse/python-challenge/PyBank/Analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
changes_net = 0
changes_average = 0
greatest_increase = 0
greatest_decrease = 0
change = 0
sum_of_changes = 0
# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data, delimiter= ',')

    # Skip the header row
    header = next(reader)
    
    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months = 1
    previous_value = int(first_row[1])
    total_net = previous_value
    # Track the total and net change

    # Process each row of data
    for row in reader:
        
        # Track the total
        total_months = total_months + 1
  
        # Track the net change
        total_net = total_net + int(row[1])

         # Track the monthly change
        change = int(row[1]) - previous_value
        previous_value = int(row[1])
        sum_of_changes = change + sum_of_changes
        
        # Calculate the greatest increase in profits (month and amount)
        
        if change > greatest_increase:
            greatest_month = row[0]
            greatest_increase = change 

        # Calculate the greatest decrease in losses (month and amount)
        if change < greatest_decrease:
            lowest_month = row[0]
            greatest_decrease = change 


# Calculate the average net change across the months
changes_average = sum_of_changes / (total_months - 1)

# Generate the output summary


# Print the output
print("Financial Analysis")
print("-----------------------------")
print("Total Months: ", total_months)
print("Total: $ ", total_net)
print("Average Change: $ ", changes_average)
print("Greatest Increase in Profits: ", greatest_month, "($",greatest_increase,")")
print("Greatest Decrease in Profits: ", lowest_month, "($",greatest_decrease,")")


output = (
    "Financial Analysis\n"
    "-----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${changes_average}\n"
    f"Greatest Increase in Profits: {greatest_month} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {lowest_month} (${greatest_decrease})\n")

# Write the output to the text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
