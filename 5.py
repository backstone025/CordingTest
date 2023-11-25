class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 0

        def spread(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i + 1 : j]

        res = ""
        for i in range(len(s)):
            res = max(spread(i, i), spread(i, i + 1), res, key=len)

        return res


a = Solution()
print(a.longestPalindrome("babad"))