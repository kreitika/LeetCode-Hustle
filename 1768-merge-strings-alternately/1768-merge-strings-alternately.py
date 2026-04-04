class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pt_1, pt_2 = 0,0
        answer = []
        count = 0
        while pt_1 < len(word1) and pt_2 < len(word2) :
            if count % 2 == 0: 
                answer.append(word1[pt_1])
                pt_1+=1
            else:
                answer.append(word2[pt_2])
                pt_2+=1
            count += 1
        while pt_1 < len(word1):
            answer.append(word1[pt_1])
            pt_1 += 1
        while pt_2 < len(word2):
            answer.append(word2[pt_2])
            pt_2 += 1

        final = ''.join(answer)
        return final