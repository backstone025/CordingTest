class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        result = []
        for idx, itv in enumerate(intervals):
            if idx == 0:
                result.append(itv)
            elif itv[0] <= result[-1][1]:
                if itv[1] <= result[-1][1]:
                    continue
                else:
                    result[-1][1] = itv[1]
            else:
                result.append(itv)
        return result