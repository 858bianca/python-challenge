# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os


print((os.getcwd()))


# Files to load and output (update with correct file paths)
file_to_load = os.path.join( "PyBank","Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join( "PyBank","analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
prev_total = 0
monthly_change = []
total_net = 0
total_change = []
greatest_inc = ["", 0]
greatest_dec = ["", 99999999999999999999]
# Add more variables to track other necessary financial data

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data, delimiter=",")
    print(reader)

    # Skip the header row
    header = next(reader)
    print(f"CSV Header: {header}")

    # Extract first row to avoid appending to net_change_list
    for row in reader:
        print(row)
        i = total_months 
    # Track the total and net change
        total_months += 1
        i = total_net
        total_net= total_net + int(row[1])
        i= total_change
        total_change = int(row[1])

    # Process each row of data
    for row in reader:

        # Track the total
        i = total_months
        total_months = total_months + 1
        i = total_net
        total_net= total_net + int(row[1])

        # Track the net change
        i= profit_change
        profit_change = prev_total + int(row[1])
    
        total_change = total_change + profit_change
    monthly_change = [row[0]]



        # Calculate the greatest increase in profits (month and amount)
   # Track the net change
    profit_change = int(row[1]) - prev_total
    prev_total = int(row[1])
    total_change = total_change + profit_change
    monthly_change = [row[0]]



        # Calculate the greatest increase in profits (month and amount)
    if (profit_change > greatest_inc[1]):
            greatest_inc[0] = row[0]
            greatest_inc[1] = profit_change

        # Calculate the greatest decrease in losses (month and amount)
    if (profit_change < greatest_dec[1]):
            greatest_dec[0]= row[0]
            greatest_dec[1]= profit_change



# Calculate the average net change across the months
profit_avg = (total_change) / (total_net)

# Generate the output summary
output =(
f"\nFinancial Analysis\n"
f"-----------------------------\n"
f"Total Months: {total_months}\n"
f"Total: {total_net}\n"
f"Average Change: ${profit_avg}\n"
f"Greatest Increase in Profits: {greatest_inc[0]} (${greatest_inc[1]})\n"
f"Greatest Decrease in Profits: {greatest_dec[0]} (${greatest_dec[1]})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)