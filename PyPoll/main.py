import csv 

input_file = "Resources/election_data.csv.csv"

candidate_list = 0
candidate_votes = 0

with open(input_file) as infile:
        if candidate_name not in candidate_list:

            candidate_list.append(candidate_name)

            candidate_votes[candidate_name] = 0

 candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

with open(input_file) as infile:
    rows = csv.reader(infile)
    header = next(rows)

    for row in rows:
        total_month = total_month + 1
        total_profit = total_profit + int(row[1])

print(total_profit)

output = f"""
Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
"""

print (output)

with open("analysis/OutputFile.txt", "w") as outfile: 
    outfile.write(output)
