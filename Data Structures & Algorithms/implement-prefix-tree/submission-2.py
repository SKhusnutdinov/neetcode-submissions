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
            if ch not in curNode.children:
                curNode.children[ch] = TrieNode()
            curNode = curNode.children[ch]
        curNode.endOfWord = True

    def search(self, word: str) -> bool:
        curNode = self.root
        for ch in word:
            if ch not in curNode.children:
                return False
            curNode = curNode.children[ch]
        return curNode.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curNode = self.root
        for ch in prefix:
            if ch not in curNode.children:
                return False
            curNode = curNode.children[ch]
        return True
        