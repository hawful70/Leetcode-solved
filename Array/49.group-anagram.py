from typing import Collection, List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = Collection.defaultdict(list)

        for str in strs:
           key = self.getKey(str)
           groups[key].append(str)

        return groups.values()

    def getKey(self, key):
        return "".join(sorted(key)) 