class Solution:
    def sortColor(self, color_list):
        for i in range(len(color_list)):
            for j in range(1, len(color_list)-i):
                if color_list[j-1] > color_list[j]:
                    color_list[j], color_list[j-1] = color_list[j-1], color_list[j]
        return color_list

a = Solution()
a.sortColor([2, 0, 2, 1, 1, 0])
a.sortColor([2, 0, 1])