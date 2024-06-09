'''
Weak passwords are likely to be hacked and misused. Due to this, developers at Amazon regularly come up with new algorithms to check the health of user passwords. A new algorithm estimates the variability of a password as the number of distinct password strings that can be obtained by reversing any one substring of the original password. Given the original password that consists of lowercase English characters, find its variability.
Note: A substring is a contiguous sequence of characters within a string. For example 'bcd', 'a', 'abcd' are substrings of the string 'abcd' whereas the strings 'bd', 'acd' are not.

Function Description
Complete the function countDistinctPasswords in the editor below.
countDistinctPasswords has the following parameter:
string password : the original password

Returns
long integer: the number of distinct password strings that can be formed

Example 1 :
Input: password = "abc"
Output: 4 
Explanation: The following strings can be formed from password = 'abc':
Reversing any substring of length 1 gives the original string "abc".
Reversing the substring "ab" gives a new string "bac".
Reversing the substring "bc" gives a new string "acb".
Reversing the substring "abc" gives a new string "cba".
There are 4 distinct password strings that can be obtained from password. Return 4.

Example 2 :
Input: password = "abaa"
Output: 4 
Explanation: The strings that can be formed are "abaa", "aaba", "baaa" and "aaab".

Constraints:
All characters in password are lowercase English letters ascii[a-z]
1 ≤ length of password ≤ 10^5
'''
def countDistinctPasswords(password):
    distinct_passwords = set()
    n = len(password)
    
    # Loop through all possible substrings
    for i in range(n):
        for j in range(i, n):
            # Reverse the substring password[i:j+1]
            new_password = password[:i] + password[i:j+1][::-1] + password[j+1:]
            # Add the new password to the set
            distinct_passwords.add(new_password)
    
    return len(distinct_passwords)

# Example usage
print(countDistinctPasswords("abc"))  # Output: 4
print(countDistinctPasswords("abaa"))  # Output: 4
