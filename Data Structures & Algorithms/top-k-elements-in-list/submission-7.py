class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countsNums = {}
        #[1,1,1, 2,2 ,3]
        #[1, 2, 3]
        #[4,3]

        nums.sort()
        for i in nums: 
            countsNums[i] = countsNums.get(i, 0) + 1

        mostApps = sorted(list(countsNums.values()))[-k:]
        
        return sorted([k for k,v in countsNums.items() if v in mostApps])
        