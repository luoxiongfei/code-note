class Solution:
    def sortString(self, s: str) -> str:
        flg = [0 for i in range(30)]
        for i in s:
            flg[ord(i) - ord('a')] += 1
        ans = ""
        while len(ans) != len(s):
            if len(ans) != len(s):
                for i in range(30):
                    if flg[i]:
                        flg[i] -= 1
                        ans += chr(i + ord('a'))
            if len(ans) != len(s):
                for i in reversed(range(30)):
                    if flg[i]:
                        flg[i] -= 1
                        ans += chr(i + ord('a'))
        return ans
