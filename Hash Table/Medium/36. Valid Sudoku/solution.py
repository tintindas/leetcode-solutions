from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSets = [set() for _ in range(9)]
        colSets = [set() for _ in range(9)]
        boxSets = [set() for _ in range(9)]

        def boxNumber(col, row):
            return (row // 3) * 3 + col // 3

        for row in range(9):
            for col in range(9):
                char = board[row][col]
                if char != ".":

                    if char not in rowSets[row]:
                        rowSets[row].add(char)
                    else:
                        return False

                    if char not in colSets[col]:
                        colSets[col].add(char)
                    else:
                        return False

                    boxIndex = boxNumber(row, col)

                    if char not in boxSets[boxIndex]:
                        boxSets[boxIndex].add(char)
                    else:
                        return False

        return True