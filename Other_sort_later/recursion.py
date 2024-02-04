# Factorial Program:
# by using for loop and without loop

n = int(input("Enter the number"))
# fact = 1
# for i in range(1, n+1):
#     fact = fact * i
# print(fact)

# By using recursion mehtod

def fact(n):
    if n == 0:
        return 1
    # factnum = fact(n-1)
    # factnum = factnum * n
    # return factnum
    return n * fact(n-1)

a = fact(n)
print(a)
