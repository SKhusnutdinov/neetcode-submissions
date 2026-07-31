class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        q = deque([beginWord])

        res = 0

        while q:
            res += 1
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                
                for i in range(len(word)):
                    for ch in range(ord('a'), ord('z') + 1):
                        if chr(ch) == word[i]:
                            continue
                        
                        changedWord = word[:i] + chr(ch) + word[i + 1:]
                        if (changedWord in words):
                            q.append(changedWord)
                            words.remove(changedWord)


        return 0

