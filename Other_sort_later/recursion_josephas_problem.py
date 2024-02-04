# def jos(n, k):

#     if n == 1:
#         return 1
#     # return (jos(n-1, k) + k-1)%n + 1
#     a = jos(n-1, k)
#     b = a + (k-1)
#     c = b % n
#     d = c + 1
#     return d
n = int(input("Eneter the n number"))
k = int(input("Enter the k number"))
# e = jos(n, k)
# print(e)

def jos(n, k):
    if n == 1:
        return 0
    return((jos(n-1, k)+k)%n )

a = jos(n, k)
print(a+1)