import os
import csv
#variable instantiation
Total=0
CandCount={}
#csv path reader, home directory
csvpath = os.path.join("election_data.csv")
#text file writer, home directory
output_path = os.path.join("pypoll.txt")

#begin reading file
with open(csvpath, "r") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #Read threw file collect the data
    for row in csvreader:
        #Running total votes counter
        Total=Total+1
        if row[2] in CandCount:
            CandCount[row[2]]+=1
        else:
            CandCount[row[2]] = 1 

#Results printed to terminal
print("Election Results")
print("-----------------------------")
print("Total Votes: " + str(Total))
print("-----------------------------")
for key, value in CandCount.items():
    print(key + ": " + "%.4f" %(CandCount.get(key) * 100/Total) + "% (" + str(value) + ")")
print("-----------------------------")
print("Winner: " + max(CandCount, key=CandCount.get))
print("-----------------------------")

#write file details
file=open(output_path, "w")
#Text file lines to write
file.write("Election Results\n")
file.write("-----------------------------\n")
file.write("Total Votes: " + str(Total) + "\n")
file.write("-----------------------------\n")
for key, value in CandCount.items():
    file.write(key + ": " + "%.4f" %(CandCount.get(key) * 100/Total) + "% (" + str(value) + ")\n")
file.write("-----------------------------\n")
file.write("Winner: " + max(CandCount, key=CandCount.get) + "\n")
file.write("-----------------------------\n")