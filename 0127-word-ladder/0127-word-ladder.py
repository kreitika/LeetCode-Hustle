class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        word_set = set(wordList)

        if endWord not in word_set : return 0

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            word, length = queue.popleft()
            if word == endWord : return length

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + c + word[i + 1 :]

                    if newWord in word_set and newWord not in visited:
                        queue.append((newWord, length + 1))
                        visited.add(newWord)


        return 0

