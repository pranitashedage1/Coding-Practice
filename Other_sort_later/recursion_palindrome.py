# without recursion

str1 = input("Enter the string")
# if str1 == str1[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

def comp(str1, start=0, end=len(str1)-1):
    if start == end or start > end:
        return "palindrome"
    if str1[start] != str1[end]:
        return "Not a palindrome"
    return comp(str1, start+1, end-1)
print(comp(str1))