class Solution:
    @classmethod
    def findOverlapElemIndex(cls, s: str) -> int:
        hash = {}

        for alpha in s:
            hash[alpha] = []

        for i in range(len(s)):
            hash[s[i]].append(i)

        return hash

    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = Solution.findOverlapElemIndex(s)

        arr = []
        res = []

        i, l = 0, 0
        length = len(s)
        while i < length:
            if s[i] not in arr:
                l += 1
                arr.append(s[i])
                i += 1
            else:
                res.append(l)
                l = 0
                index = hash[s[i]].index(i) - 1
                i = hash[s[i]][index] + 1
                arr = []
        if l != 0:
            res.append(l)
        if res == []:
            return 0
        return max(res)


