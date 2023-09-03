import re


class Solution:
    def reverseWords(self, s: str) -> str:
        def reverseUtility(arr, start, end):
            i = start
            j = end

            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        s = re.sub(' +', ' ', s.strip())

        my_str = list(s)

        reverseUtility(my_str, 0, len(s) - 1)

        start = 0
        end = 0

        while start < len(my_str):
            while end < len(my_str) and my_str[end] != ' ':
                end += 1

            reverseUtility(my_str, start, end - 1)
            start = end + 1
            end += 1

        return ''.join(my_str)
    
solution = Solution()
print(solution.reverseWords("  hello world  "))