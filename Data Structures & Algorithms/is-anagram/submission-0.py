class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26
        if len(s) != len(t):
            return False
        for chars, chart in zip(s, t):
            ind1 = ord(chars) - ord('a')
            ind2 = ord(chart) - ord('a')
            count[ind1] += 1
            count[ind2] -= 1
        return all(x == 0 for x in count)