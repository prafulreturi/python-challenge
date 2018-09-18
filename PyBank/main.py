import os

# Module for reading CSV files
import csv

file_to_read = os.path.join( 'Resources', 'budget_data.csv')

file_to_write = os.path.join( 'Analysis', 'budget_analysis.txt')

with open(file_to_read, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    has_header = csv.Sniffer().has_header(csvfile.read(1024))
    csvfile.seek(0)  
    reader = csv.reader(csvfile)
    if has_header:
        next(reader)
    financial_data_list = list(csvreader)
 

# Convert profit element to int
financial_data_list_converted = list(map(lambda x: [x[0], int(x[1])], financial_data_list))

key_value_list = []
profit_change_list = [] 
months_list = []
profits_list = []

# Unpack nested list to months list and profit list 

for i in range(len(financial_data_list_converted)):
   if i == len(financial_data_list_converted):
       break
   else:
           months_list.append(financial_data_list_converted[i][0])
           profits_list.append(financial_data_list_converted[i][1])
           i += 1

# Loop through financial data converted list to find profit change over each period.

for i in range(len(financial_data_list_converted)):
   if i == len(financial_data_list_converted) - 1:
       break
   else:
           value_change = financial_data_list_converted[i+1][1] - financial_data_list_converted[i][1]
           month = financial_data_list_converted[i+1][0]
           key_value_list.append([month,value_change])
           profit_change_list.append(value_change)
           i += 1



# Total number of months

total_months = len(months_list)

# Net amount

net_amount = sum(profits_list)

# Average change

average_change = round(sum(profit_change_list)/len(profit_change_list),2)

# Greatest increase in profits

greatest_increase = max(key_value_list, key=lambda x: x[1])

# Greatest decrease in profits

greatest_decrease = min(key_value_list, key=lambda x: x[1])
     
# print to terminal

print(f"""
       Financial Analysis
       --------------------------------------------------
       Total Months: {total_months}
       Total: ${net_amount}
       Average Change: ${average_change}
       Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})
       Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})

        """)
 
 # write to text file   

with open("budget_analysis.txt", "w") as text_file:
    print(f"""
       Financial Analysis
       --------------------------------------------------
       Total Months: {total_months}
       Total: ${net_amount}
       Average Change: ${average_change}
       Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})
       Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})

        """ , 
        file=text_file)
