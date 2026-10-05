class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            alpha = [0] * 26
            for char in word:
                alpha[ord(char) - ord('a')] += 1
            key = tuple(alpha)
            if key not in groups:
                groups[key] = [word]
            else:
                groups[key].append(word)
        return list(groups.values())