class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root
        for c in word:
            if cur.children.get(c) is None:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for c in word:
            if cur.children.get(c) is None:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for c in prefix:
            if cur.children.get(c) is None:
                return False
            cur = cur.children[c]
        return True
            
# The time complexity of the Trie class's insert, search, and startsWith methods is O(m), where m is the length of the input string.
# Space complexity O(n*m), where n is the number of strings inserted into the trie and m is the average length of the strings.

# Space expanation: This is because for each character in each string, we create a new node in the trie. Therefore, the total number of nodes in the trie is proportional to the total number of characters in all the strings, which is n * m.


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)