class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)

        q = deque()
        q.append(beginWord)

        visit = set()
        res = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                
                visit.add(word)
                wordForm = list(word)
                
                for i in range(len(word)):
                    changeWordForm = wordForm.copy()
                    for ch in range(ord('a'), ord('z') + 1):
                        changeWordForm[i] = chr(ch)
                        changedWord = "".join(changeWordForm)
                        print(changedWord)
                        if (changedWord in words and
                            changedWord not in visit
                            ):
                            q.append(changedWord)

            res += 1

        return 0

