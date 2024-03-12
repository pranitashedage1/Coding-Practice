# 0, 1, 1, 2, 3, 5, 8, ....
# print(0, 1, end = " ")
# def fib(a, b):
#     print(a+b, end = " ")
#     if (a+b) > 20:
#         return
#     fib(b,a+b)

# fib(0,1)

count = 0
print(0, 1, end = " ")
def fib(a, b, count):
    count += 1 
    if count > 10-2:
        return
    print(a+b, end = " ")
    fib(b,a+b, count)

fib(0,1, 0)

# F(3) = F(2) + F(1) > 1 + 1 = 2
# F(4) = F(3) + F(2) > 2 + 1 = 3
# F(2) = F(2) + F(1) > 1 + 0 = 1

# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# b = fibonacci(5)
# print(b)

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

