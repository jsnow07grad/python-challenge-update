import csv 

input_file = "Resources/budget_data.csv"

total_month = 0
total_profit = 0
previous_profit = 0
total_change = 0
change = 0
change_counter = 0
greatest_increase = 0
greatest_increase_month = ""
greatest_decrease = 0
greatest_decrease_month = ""

with open(input_file) as infile:
    rows = csv.reader(infile)
    header = next(rows)

    for row in rows:
        total_month = total_month + 1
        total_profit = total_profit + int(row[1])
        current_profit = int(row[1])

        if previous_profit != 0:
            change = current_profit - previous_profit 
            total_change = total_change + change
            change_counter = change_counter + 1

        previous_profit = current_profit

        if change>greatest_increase: 
            greatest_increase = change
            greatest_increase_month = row[0]

        if change<greatest_decrease:            
           greatest_decrease = change
           greatest_decrease_month = row[0]
 
print(round(total_change/change_counter,2))

output = f"""
Financial Analysis
----------------------------
Total Months: {total_month}
Total: ${total_profit}
Average Change: ${total_change/change_counter:.2f}
Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})
Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})
"""

print (output)

with open("analysis/OutputFile.txt", "w") as outfile: 
    outfile.write(output)
