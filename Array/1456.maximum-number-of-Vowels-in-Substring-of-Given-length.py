class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        maxVowels = currentMaxVowels = 0
        
        for i, c in enumerate(s):
            if c in vowels:
                currentMaxVowels += 1
            if i >= k and s[i - k] in vowels:
                currentMaxVowels -= 1
            maxVowels = max(maxVowels, currentMaxVowels) 
        
        return maxVowels