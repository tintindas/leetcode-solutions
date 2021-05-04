from typing import List


class Solution:
    def dfs(self, board, word, row, col, idx):
        if idx == len(word):
            return True
        
        if row < 0 or row >= self.m or col < 0 or col >= self.n or word[idx] != board[row][col]:
            return False
        
        temp = board[row][col]
        board[row][col] = ' '
        print(temp)
        
        found = (self.dfs(board, word, row - 1, col, idx + 1) or
                self.dfs(board, word, row, col + 1, idx + 1) or
                self.dfs(board, word, row + 1, col, idx + 1) or
                self.dfs(board, word, row, col - 1, idx + 1))
        
        board[row][col] = temp
        
        return found
        
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        self.m, self.n = m, n
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.dfs(board, word, i, j, 0):
                        return True
        
        return False