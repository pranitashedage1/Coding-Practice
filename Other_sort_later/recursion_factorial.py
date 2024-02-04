# with loop or without loop
n = int(input("Enter the number"))
# fact = 1
# for i in range(1, n+1):
#     fact = fact * i
# print(fact)


# with recursion
def fun1(n):
    if n == 1:
       return 1
    return fun1(n-1) * n
print(fun1(n))