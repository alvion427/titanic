import csv

dataRows = []

inputFile = open('titanic_data.csv', 'r')
reader = csv.reader(inputFile)
dataRows = [row for row in reader]


print(f"I found {len(dataRows)} rows")
print(f"Column Headers: {dataRows[0]}")
print(f"First Row: {dataRows[1]}")

print("Ok chandler, now load these rows into numpy/pandas and so some analysis!!!")

inputFile.close()