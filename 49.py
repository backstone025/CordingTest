from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        d = defaultdict(list)

        for str in strs:
            d[''.join(sorted(str))].append(str)

        return list(d.values())

a = Solution()
a.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
