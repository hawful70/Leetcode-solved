from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9

        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        blocks = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(N):
            for c in range(N):
                currentBox = board[r][c]
                if currentBox == ".":
                    continue

                if (currentBox in rows[r]) or (currentBox in cols[c]) or (currentBox in blocks[r // 3][c // 3]):
                    return False

                rows[r].add(currentBox)
                cols[c].add(currentBox)
                blocks[r // 3][c // 3].add(currentBox)
        return True 