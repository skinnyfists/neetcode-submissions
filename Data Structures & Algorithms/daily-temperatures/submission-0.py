class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for day, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                popped_temp, popped_day = stack.pop()
                result[popped_day] = day - popped_day
            stack.append((temp, day))
        return result