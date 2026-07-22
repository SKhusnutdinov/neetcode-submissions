class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curNode = self.root
        for ch in word:
            if ch in curNode.children:
                curNode = curNode.children[ch]
            else:
                newNode = TrieNode()
                curNode.children[ch] = newNode
                curNode = newNode
        curNode.endOfWord = True

    def search(self, word: str) -> bool:
        curNode = self.root
        for ch in word:
            if ch in curNode.children:
                curNode = curNode.children[ch]
            else:
                return False
        return curNode.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curNode = self.root
        for ch in prefix:
            if ch in curNode.children:
                curNode = curNode.children[ch]
            else:
                return False
        return True
        