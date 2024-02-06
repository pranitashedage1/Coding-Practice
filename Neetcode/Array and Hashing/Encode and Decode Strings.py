'''
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:
string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:
string encoded_string = encode(strs);

and Machine 2 does:
vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.
You are not allowed to solve the problem using any serialize methods (such as eval).
'''
# Firest approach - 
# Time complexity - O(n)
#  Space complexity - O(k)
class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        encoded_string = ''
        for s in strs:
            encoded_string += s.replace('/', '//') + '/:'
        return encoded_string

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        list1 = []
        word = ''
        i = 0
        while i < len(s):
            if (s[i] == '/' and s[i+1] == '/'):
                word += '/'
                i += 2
            elif (s[i] == '/' and s[i+1] == ':'):
                list1.append(word)
                word = ''
                i += 2
            else:
                word += s[i]
                i += 1

        return list1

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

# TODO: Second Approach -
    