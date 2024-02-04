# print n to 1 with or without loop:
n = int(input("Enter the number"))
# for i in range(n, 0, -1):
#     print(i)

# with recursion
# def fun1(n):
#     print(n)
#     if n > 1:
#         fun1(n-1)

# fun1(n)

# with recursion
def fun2(n):
    print(n)
    if n > 1:
        fun2(n-1)
    print(n)

fun2(n)