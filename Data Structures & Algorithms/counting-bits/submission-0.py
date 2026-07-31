class Solution:
    def countBits(self, n: int) -> List[int]:
        return [sum((1 for i in range(32) if 1 << i & num)) for num in range(n + 1)]