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

