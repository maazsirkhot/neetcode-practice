class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1

        maximumArea = 0

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)

            maximumArea = max(maximumArea, area)

            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
                right -= 1

        return maximumArea
        