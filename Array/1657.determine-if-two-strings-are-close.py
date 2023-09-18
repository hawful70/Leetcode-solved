from collections import Counter, defaultdict


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        dic1, dic2 = defaultdict(int), defaultdict(int)

        for i in range(len(word1)):
            dic1[word1[i]] += 1
        for i in range(len(word2)):
            dic2[word2[i]] += 1
        
        frequency1, frequency2 = [], []
        for key in dic1:
            frequency1.append(dic1[key])
        for key in dic2:
            frequency2.append(dic2[key])

        frequency1 = Counter(frequency1)
        frequency2 = Counter(frequency2)
        
        key1, key2 = set(word1), set(word2)

        return key1 == key2 and frequency1 == frequency2
        
    
solution = Solution()
#print(solution.closeStrings("cabbba", "abbccc"))
print(solution.closeStrings("aaabbbbccddeeeeefffff", "aaaaabbcccdddeeeeffff"))
        

        