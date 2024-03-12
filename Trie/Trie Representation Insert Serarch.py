class TrieNode:
    def __init__(self) -> None:
        self.children = [None] * 26
        self.isEndOfWord = False

class Trie:
    def __init__(self) -> None:
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()
    
    def _charToIndex(self, ch):
        return ord(ch) - ord(ch)
    
    def insert(self, key):
        pCrawl = self.root
        len_of_word = len(key)

        for level in range(len_of_word):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
        pCrawl.isEndOfWord = True
    
    def search(self, key):
        pCrawl = self.root
        len_of_word = len(key)

        for level in range(len_of_word):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
        return pCrawl.isEndOfWord
        
if __name__ =='__main__':
    keys = ['bad', 'bat', 'cut', 'cat','geeks', 'zoo']
    t = Trie()
    test = ['Not Found', 'Found']
    for key in keys:
        t.insert(key)

    print('test', t.search('test'))
    print('cat', t.search('cat'))
