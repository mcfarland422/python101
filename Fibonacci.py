# fibList = [1, 2]
#
# for i in range (2, 10):
#     x = fibList[i-1] + fibList[i-2]
#     fibList.insert(i, x)
# print fibList

fibList = []
sumFib = 2

for i in range (2,10):
    x = fibList[i-1] + fibList[i-2]
    fibList.insert(i,x)
    if (fibList[i]%2 == 0):
        sumFib += fibList[i]
    if (i >= 4000000):
        break;

print fibList
print i
print sumFib
