class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countsNums = {}

        for i in nums: 
            countsNums[i] = countsNums.get(i, 0) + 1

        mostApps = sorted(list(countsNums.values()))[-k:]
        return [k for k,v in countsNums.items() if v in mostApps]
        