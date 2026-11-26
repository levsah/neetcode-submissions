class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        ## set up a list of words to add to return
        res = []
        i = 0
        ## think about how long you want to iterate until
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length_of_word = int(s[i:j]) # '5'
            j += 1
            res.append(s[j:j+length_of_word])
            i = j + length_of_word
        return res