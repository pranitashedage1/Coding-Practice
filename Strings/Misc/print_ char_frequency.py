# PPrint the frequency of the character from the word.
# Print the smallest character first and then largest character.
# e should print first then in the end s should print

word = 'geeksforgeeks'
chars = [0] * 26
print(chars)
for i in range(len(word)):
    count =  ord(word[i]) - ord('a')
    chars[count] += 1
print(chars)
for i in range(26):
    if chars[i]>0:
        print(chr(i + ord('a')), chars[i])
