from heapq import heapify, heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        heapify(heap)
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        for num, count in frequency.items():
            heappush(heap, (count, num))
            if len(heap) > k:
                heappop(heap)
        return [num for _count, num in heap]