class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        n = len(s)
        memo = {}

        def backtrack(start):
            if start in memo :
                return memo[start]

            if start == n:
                return ['']
            
            sentences = []

            for end in range(start + 1, n + 1):
                word = s[start : end]

                if word in word_set :
                    rest_sentences = backtrack(end)
                
                    for rest in rest_sentences:
                        if rest == '': sentences.append(word)
                        else:
                            sentences.append(word + ' ' + rest)

            memo[start] = sentences
            return sentences

        return backtrack(0)


        