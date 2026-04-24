class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        count2 = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

        # build s1 and first window of s2
        for i in range(len(s1)):
            count1[s1[i]] += 1
            count2[s2[i]] += 1

        # count matches
        matches = 0
        for c in count1:
            if count1[c] == count2[c]:
                matches += 1

        L = 0
        for R in range(len(s1), len(s2)):
            if matches == 26:
                return True

        # add new char
            char = s2[R]
            count2[char] += 1
            if count2[char] == count1[char]:
                matches += 1
            elif count2[char] == count1[char] + 1:
                matches -= 1

        # remove left char
            char = s2[L]
            count2[char] -= 1
            if count2[char] == count1[char]:
                matches += 1
            elif count2[char] == count1[char] - 1:
                matches -= 1

            L += 1

        return matches == 26