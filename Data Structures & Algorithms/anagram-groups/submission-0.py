class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            final[sorted_word].append(word)
        return list(final.values())
        
        





        