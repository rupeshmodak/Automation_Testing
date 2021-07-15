import csv

with open('utilities/loanCSV') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    names = []
    status = []
    for row in csvReader:
        print(row)
        names.append(row[0])
        status.append(row[1])
print(names)
print(status)

print("________________________________________")

index = names.index('Siddhesh')
loanStatus = status[index]
print("Loan status is "+loanStatus)

print("________________________________________")

with open('utilities/loanCSV', 'a') as writeFile:
    write = csv.writer(writeFile)
    write.writerow(["Vinita", "Approved"])

