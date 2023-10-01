from typing import Collection


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # counterS = Counter(s)
        # counterT = Counter(t)
        # for c in t:
        #     if c not in counterS:
        #         return False
        #     if counterS[c] != counterT[c]:
        #         return False
        # return True

        #return sorted(s) == sorted(t)
        counter = Collection.defaultdict(int)
        for c in s:
            counter[c] += 1
        for c in t:
            counter[c] -= 1
        for val in counter.values():
            if val != 0:
                return False
        return True
        
            
        

        
