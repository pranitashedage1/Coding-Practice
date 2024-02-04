n = int(input("Enter the number"))

def findsum(n):
    if n < 10:
        return n
    return findsum(int(n/10)) + n%10 

a = findsum(n)
print(a)