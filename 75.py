class Solution:
    def sortColor(self, color_list):
        res = sorted(color_list)
        print(res)
        return res

a = Solution()
a.sortColor([2, 0, 2, 1, 1, 0])
a.sortColor([2, 0, 1])