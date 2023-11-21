class Solution:
    def sortColor(self, color_list):
        for i in range(len(color_list)):
            for j in range(i-1, -1, -1):
                if color_list[j+1] <= color_list[j]:
                    color_list[j+1], color_list[j] = color_list[j], color_list[j+1]
        print(color_list)
        return color_list

a = Solution()
a.sortColor([2, 0, 2, 1, 1, 0])
a.sortColor([2, 0, 1])