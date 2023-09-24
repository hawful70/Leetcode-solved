import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        stringBuilder = []

        collection_counter = collections.Counter(s)

        for key, value in collection_counter.most_common():
            stringBuilder.append(key * value)

        return "".join(stringBuilder)
    
solution = Solution()
print(solution.frequencySort("tree"))