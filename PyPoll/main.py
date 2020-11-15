import csv
filename = './Resources/elections_data.csv'

electionsData = []
with open(filename,"r") as data:
    elections = csv.reader(data)
    hdr = next(elections)
    for row in elections:
        electionsData.append(row)

totalVotes = len(electionsData)
mostVotes = 0

electionDict = {}

for i in range(len(electionsData)):
    if electionsData[i][2] in electionDict:
        electionDict[electionsData[i][2]] += 1
    else:
        electionDict[electionsData[i][2]] = 1


votes = list(electionDict.items())

for item in votes:
    if item[1] > mostVotes:
        mostVotes = item[1]
        winner = item[0]


print('Election Results')
print('-------------------------')
print('Total Votes: ', totalVotes)
print('-------------------------')
for item in votes:
    print(item[0], ':', round(item[1]*100/totalVotes,3),'% (',item[1],')')

print('-------------------------')
print('Winner: ', winner)
print('-------------------------')
