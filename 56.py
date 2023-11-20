class Solution:
    def merge(self, intervals):
        result = []
        intervals.sort()
        index = 0
        while index < len(intervals):
            temp = []
            start = intervals[index][0]
            end = intervals[index][1]
            j = index + 1
            while j < len(intervals) and end >= intervals[j][0]:
                end = max(intervals[j][1], end)
                index = j
                j += 1
            temp.append(start)
            temp.append(end)
            result.append(temp)
            index += 1

        print(result)
        return result

a = Solution()
a.merge([[1, 3], [2, 6], [8, 10], [15, 18]])