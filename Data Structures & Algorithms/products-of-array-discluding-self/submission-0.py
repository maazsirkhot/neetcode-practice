class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        result = [1] * l

        for i in range(1, l):
            result[i] = nums[i - 1] * result[i - 1]

        right = 1
        for j in range(l-1, -1, -1):
            result[j] = right * result[j]
            right *= nums[j]

        return result
