class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}

        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

        lst = []
        for n, shows_up in counts.items():
            lst.append([shows_up, n])

        ans = []
        for subl in sorted(lst, reverse=True)[:k]:
            ans.append(subl[1])
        return ans









        
        
        
