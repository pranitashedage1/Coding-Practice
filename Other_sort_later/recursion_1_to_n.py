# with loop and without loop
n = int(input("Enter the number"))
# for i in range(1, n+1):
#     print(i)


# without loop
# def fun1(n, num = 1):
#     if num <= n:
#         print(num)
#         fun1(n, num+1)
# fun1(n)

# Witout loop:
# def fun2(n):
#     if n >= 1:
#         fun2(n-1)
#     print(n)

# fun2(n)

# without loop
# def fun3(n):
#     if n == 0:
#         return
#     fun3(n-1)
#     print(n)
# fun3(n)

# without loop
# def fun4(n, num=1):
#    if num > n:
#         return
#    print(num)
#    fun4(n, num+1)
# fun4(n)

def fun5(n, num=1):
    if n < 1:
        return
    print(num)
    fun5(n-1, num+1)
fun5(n)