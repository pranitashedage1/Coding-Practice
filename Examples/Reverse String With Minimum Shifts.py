'''
AWS stores grayscale images as an array of white and black pixels. The image is stored as a binary string where a white pixel is represented by '1', and a black pixel is represented by '0'. The reverse of the image is represented as the reverse of this binary representation. For example, the reverse of "11010" is "01011". They want to store the reverse of each image as a backup. In order to reproduce the reverse from the original, the following operation can be performed any number of times: remove any character from the string and append it to the end of the string, i.e., choose any pixel and shift it to the end of the string.
Given the binary representation of pixels denoted by image, find the minimum number of operations needed to produce its reverse.

Function Description
Complete the function findMinimumOperations in the editor.
findMinimumOperations has the following parameter:
String image : a binary string that represents an image

Returns
int : the minimum number of operations required to produce a reverse, i.e., to reverse the string.

Example 1 :
Input: image = "0100110"
Output: 3 
Explanation: The reverse of the image, i.e., the reverse of the string, is "0110010", and it can be produced using the sequence of operations shown in the image above : The string cannot be reversed in fewer than 3 operations. Return 3.

'''
def findMinimumOperations(image: str) -> int:
    reversed_image = image[::-1]
    n = len(image)
    
    # Find the longest suffix of 'reversed_image' that matches a prefix of 'image'
    i, j = 0, 0
    while i < n and j < n:
        if image[i] == reversed_image[j]:
            j += 1
        i += 1
    # The minimum number of operations required is the total length of the image minus the length of the matching suffix
    return n - j

# Example usage
image = "0100110"
print(findMinimumOperations(image))  # Output: 3