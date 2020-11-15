import csv
filename = './Resources/budget_data.csv'

budgetData = []
with open(filename,"r") as data:
    bank = csv.reader(data)
    hdr = next(bank)
    for row in bank:
        budgetData.append(row)

totalMonths = len(budgetData)
netTotal = 0

for item in budgetData:
    netTotal += int(item[-1])

changePerPeriod = list()

for i in range(1, len(budgetData)):
    change = int(budgetData[i][-1]) - int(budgetData[i - 1][-1])
    changePerPeriod.append(change)

maxIncrease = 0
maxDecrease = 0

maxIncMonth = ''
macDecMonth = ''

avgChng = sum(changePerPeriod)/len(changePerPeriod)

for pos, change in enumerate(changePerPeriod):
    if change > maxIncrease:
        maxIncrease = change
        maxIncMonth = budgetData[pos+1][0]
    if change < maxDecrease:
        maxDecrease = change
        maxDecMonth = budgetData[pos+1][0]

    
print('Financial Analysis')
print('----------------------------')
print('Total Months:', totalMonths)
print('Net Total:', netTotal)
print('Average', avgChng)
print('Max Increase',maxIncMonth, maxIncrease)
print('Max Decrease',maxDecMonth, maxDecrease)

      

