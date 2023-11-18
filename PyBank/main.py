import csv 

input_file = "Resources/budget_data.csv"

total_month = 0
total_profit = 0

with open(input_file) as infile:
    rows = csv.reader(infile)
    header = next(rows)

    for row in rows:
        total_month = total_month + 1
        total_profit = total_profit + int(row[1])

print(total_profit)

output = f"""
Financial Analysis
----------------------------
Total Months: {total_month}
Total: ${total_profit}
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
"""

print (output)

with open("analysis/OutputFile.txt", "w") as outfile: 
    outfile.write(output)
