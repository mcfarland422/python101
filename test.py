fibList = [1, 2]
sum = 2

# find fib list
for i in range (2, 4000000):
    # fib formula
    x = fibList[i-1] + fibList[i-2]
    # adds value to proper index value
    fibList.insert(i, x)
    #breaks once over 4mil
    if (x > 4000001):
        break
    #adds to sum if even
    if (x % 2 == 0):
        sum += x
print sum

does this code work? Maybe
