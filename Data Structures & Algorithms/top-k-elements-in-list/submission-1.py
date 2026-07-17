class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)
        for num in nums:
            freqMap[num] += 1

        heap = []
        for key, value in freqMap.items():
            heapq.heappush(heap, (value, key))
            
            if len(heap) > k:
                heapq.heappop(heap)
            print(heap)

        result = []
        for key, value in heap:
            result.append(value)

        return result
            
        