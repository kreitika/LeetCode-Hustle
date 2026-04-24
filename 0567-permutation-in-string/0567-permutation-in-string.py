class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) : return False 
        count1 = [0]*26
        count2 = [0]*26
        for i in s1:
            count1[ord(i) - ord('a')]+=1
        
        L = 0
        for R in range(len(s2)) :
            count2[ord(s2[R]) - ord('a')] += 1
            if R - L + 1 > len(s1):
                count2[ord(s2[L]) - ord('a')] -= 1
                L += 1
            if R - L + 1 == len(s1):
                if count1 == count2: return True
        return False


        