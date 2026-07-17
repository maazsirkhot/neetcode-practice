class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        size = len(nums)
        
        for l in range(size):
            if nums[l] > 0:
                break
            
            if l > 0 and nums[l] == nums[l - 1]:
                continue

            target = nums[l]

            i = l + 1
            j = size - 1

            while i < j:
                total = target + nums[i] + nums[j]
                if total > 0:
                    j -= 1
                    
                elif total < 0:
                    i += 1
                else:
                    result.append([target, nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while nums[i] == nums[i - 1] and i < j:
                        i += 1

        return result


                
