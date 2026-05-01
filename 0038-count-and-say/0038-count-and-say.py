class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1 : return "1"
        s = self.countAndSay(n - 1)
        count = 1
        ans = ""

        for num in range(1, len(s)):
            if  s[num] == s[num - 1]:
                count += 1
            else :
                temp = str(count) + str(s[num - 1])
                ans += temp
                count = 1
        temp = str(count) + s[-1]
        ans += temp
        return ans

