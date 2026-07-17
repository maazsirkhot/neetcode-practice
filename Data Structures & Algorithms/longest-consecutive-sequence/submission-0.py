class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        maxCount = 0
        for num in nums:
            if num - 1 not in hashSet:
                seq = 1
                while num + 1 in hashSet:
                    seq += 1
                    num += 1
                maxCount = max(maxCount, seq)

        return maxCount

        
        