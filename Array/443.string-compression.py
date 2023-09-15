from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        i = 0
        s = ""
        for j in range(1, len(chars)):
            if chars[i] != chars[j]:
                counter = j - i
                if counter >= 10:
                    s += chars[i]
                    counter = str(counter)
                    for char in counter:
                        s += char
                    
                else:
                    s += chars[i]
                    if counter > 1:
                        s += str(counter)
                        
                i = j
            if j == len(chars) - 1:
                counter = (j - i) + 1
                if counter >= 10:
                    s += chars[i]
                    counter = str(counter)
                    for char in counter:
                        s += char
                else:
                    s += chars[i]
                    if counter > 1:
                        s += str(counter)

        chars.clear()
        for i in range(len(s)):
            chars.append(s[i])
        return len(chars)
    
solution = Solution()
print(solution.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))


