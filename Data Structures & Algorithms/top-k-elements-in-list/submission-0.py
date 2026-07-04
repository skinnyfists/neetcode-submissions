class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        frequency_sorted = sorted(frequency.items(), key=lambda item: item[1])
        return [n for n, _f in frequency_sorted[-k:]]