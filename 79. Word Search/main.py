"""
@param {character[][]} board
@param {string} word
@return {boolean}
"""
class Solution:
    def exist(self, board: list, word: str) -> bool:
        self.board = board
        self.word = word
        self.m = len(board)
        self.n = len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j]==word[0] and self.dfs(i, j, 0):
                    return True
        return False

    def dfs(self, i , j, k):
        if k == len(self.word):
            return True
        if i < 0 or i >= self.m or j < 0 or j >= self.n or self.board[i][j]!=self.word[k]:
            return False
        self.board[i][j]="#"
        if self.dfs(i-1, j, k+1) or self.dfs(i, j-1, k+1) or self.dfs(i+1, j, k+1) or self.dfs(i, j+1, k+1):
            return True
        self.board[i][j]=word[k]

s = Solution()
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
print(s.exist(board, word))  # true

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "SEE"
print(s.exist(board, word))  # true

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCB"
print(s.exist(board, word))  # false

board = [["a", "b"], ["c", "d"]]
word = "abcd"
print(s.exist(board, word))  # false

board = [["a", "a"]]
word = "aaa"
print(s.exist(board, word))  # false

board = [["a", "b"], ["c", "d"]]
word = "acdb"
print(s.exist(board, word))  # true
