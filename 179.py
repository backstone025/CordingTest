class Solution(object):
    def largestNumber(self, nums):
        for i in range(len(nums), 0, -1):
            for j in range(0, i-1):
                if not self.compare(nums[j], nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        print(str(int("".join(map(str, nums)))))
        return str(int("".join(map(str, nums))))

    def compare(self, n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)

a = Solution()
a.largestNumber([10, 2])