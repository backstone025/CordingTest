class Solution():
    def largestNumber(self, nums):
        for i in range(len(nums)):
            for j in range(i-1, -1, -1):
                if int(str(nums[j+1]) + str(nums[j])) > int(str(nums[j]) + str(nums[j+1])):
                    nums[j+1], nums[j] = nums[j], nums[j+1]

        return str(int("".join(map(str, nums))))

a = Solution()
a.largestNumber([3, 30, 34, 5, 9])
