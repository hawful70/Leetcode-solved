from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        ans = []
        current_solution = []
        def choose(increment):
            if increment == len(digits):
                ans.append("".join(current_solution))
                return

            for next_character in letters[digits[increment]]:
                current_solution.append(next_character)
                choose(increment + 1)
                current_solution.pop()
        choose(0)

        return ans

