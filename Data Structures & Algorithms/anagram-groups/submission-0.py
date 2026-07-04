from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs = [s.lower() for s in strs]

        groups = defaultdict(list)
        for string in strs:
            frequency_map = [0] * 26
            for char in string:
                frequency_map[ord(char.lower()) - ord("a")] += 1
            groups[tuple(frequency_map)].append(string)
        return [group for group in groups.values()]