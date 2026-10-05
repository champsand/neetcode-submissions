class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Freq = {}
        bucket = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            if num not in Freq:
                Freq[num] = 1
            else:
                Freq[num] += 1
        for key, value in Freq.items():
            bucket[value].append(key)
        ans = []
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans