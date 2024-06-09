'''
A recently launched supplemental typing keypad gained significant popularity on Amazon Shopping due to its flexibility.
This keypad can be connected to any electronic device and has 9 buttons, where each button can have up to 3 lowercase English letters. The buyer has the freedom to choose which letters to place on a button while ensuring that the arrangement is valid. A keypad design is said to be valid if:
All 26 letters of the English alphabet exist on the keypad.
Each letter is mapped to exactly one button.
A button has at most 3 letters mapped to it.
Examples of some valid keypad designs are:
1 2 3 abc def ghi 4 5 6 jkl mno pqr 7 8 9 stu vwx yz
1 2 3 ajs bot cpu 4 5 6 dkv hmz gl 7 8 9 enw fqx iry
In the left keypad, "hello" can be typed using the following button presses:
[3] twice (prints 'h')
[2] twice (prints 'e')
[4] thrice (prints 'l')
[4] thrice (prints 'l')
[5] thrice (prints 'o')
Thus, total num of button presses = 2 + 2 + 3 + 3 + 3 = 13.
In the right keypad, "hello" can be typed using the following button presses:
[5] once (prints 'h')
[7] once (prints 'e')
[6] twice (prints 'l')
[6] twice (prints 'l')
[2] twice (prints 'o')
Thus, the total num of button presses = 1 + 1 + 2 + 2 + 2 = 8.
The keypad click count is defined as the number of button presses required to print a given string. In order to send messages faster, customers tend to seek the keypad design in such a way that the keypad click count is minimized while maintaining its validity.
Given a string letters consisting of lowercase English letters only, find the minimum Keypad click count.

Example 1 :
Input: letters = "abacadefghibj"
Output: 14 
Explanation:
One of the optimal keypad designs to minimize the keypad click count is:
1 2 3 ajs bkt clu 
4 5 6 dmv enw fox
7 8 9 gpy hqz ir 
Here, the keypad click count = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 2 = 14.
'''
from collections import Counter
def count(string1):
    freq = Counter(string1)
    items = [item for item in freq.items()]
    items.sort(reverse=True, key= lambda x:x[1])
    press = 0
    for index, item in enumerate(items):
        if index < 9 :
            press += 1 * item[1]
        elif index < 18:
            press += 2 * (item[1])
        elif index < 26:
            press += 3 * (item[1])

    return press


str1 = 'abacadefghibj'
print(count(str1))
str2 = 'abcdefghijklmnopqrstuvwxyz'
print(count(str2))

