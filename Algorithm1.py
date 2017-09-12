threesList = []
fivesList = []
fifteensList = []
duplicates = []

# find multiples of three

for i in range (1,1000):
    if (i%3 == 0):
        threesList.append(i)

# find multiples of five

for i in range (1,1000):
    if (i%5 == 0):
        fivesList.append(i)

# find multiples of fiftween

for i in range (1,1000):
    if (i%15 == 0):
        fifteensList.append(i)

# print threesList
# print fivesList
# print fifteensList


print(sum(threesList) + sum(fivesList) - sum(fifteensList))
