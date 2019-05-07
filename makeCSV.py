# imports
import csv
import sys
import math

# make sure we're getting the right number of arguments
if (len(sys.argv) < 5):
    print '<n-up> <needed> <startNum> <leading zeros>'
    quit()

# variables
csvData = []  # stores csv data
# variables from sys args
nUp = int(sys.argv[1])  # how many files we have up on the page
needed = float(sys.argv[2])  # how many things we're printing
startNum = int(sys.argv[3])  # what number to start at
leadingZeros = int(sys.argv[4]) + 1  # how many leading zeros

rowsNeeded = int(math.ceil(needed/nUp))  # calculate how many rows we need

# build headers
headers = []
for i in range(0, nUp):
    colName = 'col' + str(i+1)
    headers.append(colName)

csvData.append(headers)  # add headers to csv data

# build numbers array
for i in range(0, rowsNeeded):
    row = []
    for j in range(0, nUp):
        row.append(str((1 + i + (rowsNeeded * j) + startNum))
                   .zfill(leadingZeros))  # add the leading zeros if necessary
    csvData.append(row)

# build file name, split up to avoid the "lines too long" thing
fileName = str(nUp) + "up " + str(startNum) + "-"
fileName = fileName + csvData[len(csvData) - 1][nUp - 1] + ".csv"

# create and write to file
with open(fileName, 'wb') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)

csvFile.close()
print fileName + " created!"
