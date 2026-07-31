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
                    changedWordForm = list(word)
                    for ch in range(ord('a'), ord('z') + 1):
                        if chr(ch) == word[i]:
                            continue
                        changedWordForm[i] = chr(ch)
                        changedWord = "".join(changedWordForm)
                        if (changedWord in words):
                            q.append(changedWord)
                            words.remove(changedWord)


        return 0

