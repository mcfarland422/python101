# def isprime(n):  # First the primality test
#     if n<2:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#             break
#     else:
#         return True
#
# def nthprime(n):   # then generic code for nth prime number
#     x=[]
#     j=2
#     while len(x)<n:
#         if (isprime(j)) == True:
#             x.append(j)
#         j =j+1
#     print(x[n-1])
#
# this = nthprime(10001)
# print this




lower = 1
upper = 10001

print("Prime numbers between",lower,"and",upper,"are:")

for num in range(lower,upper + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
