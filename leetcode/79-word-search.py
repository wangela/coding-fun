"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.
"""
class Solution:
    def exist_helper(self, board, row, col, visited, wordlet):
        if len(board) == 0:
            return False
        if len(board[0]) == 0:
            return False
        if len(wordlet) == 0:
            return True
        trials = [-1, 1]
        moves = []
        visiting = (row, col)
        print("visiting " + str(visiting))
        print("visited " + str(visited))

        for attempt in trials:
            new_row = row + attempt
            if new_row < len(board) and new_row >= 0:
                next_coord = (new_row, col)
                if next_coord not in visited:
                    print("adding" + str(next_coord))
                    moves.append(next_coord)
            new_col = col + attempt
            if new_col < len(board[0]) and new_col >= 0:
                next_coord = (row, new_col)
                if next_coord not in visited:
                    print("adding" + str(next_coord))
                    moves.append(next_coord)

        print(wordlet)
        for move in moves:
            print(move)
            move_row = move[0]
            move_col = move[1]
            v2 = set(visited)
            coord = (move_row, move_col)
            v2.add(coord)
            if board[move_row][move_col] != wordlet[0]:
                continue
            elif self.exist_helper(board, move_row, move_col, v2, wordlet[1:]):
                return True
        return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return True

        for r, row in enumerate(board):
            for c, col in enumerate(row):
                if board[r][c] == word[0]:
                    visited = set([(r, c)])
                    if self.exist_helper(board, r, c, visited, word[1:]):
                        return True
        return False

board =[['A','B','C','E'], ['S','F','C','S'],['A','D','E','E']]
board2 = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
board3 = [["a", "a"]]
# ["A","B","C","E"],
# ["S","F","E","S"],
# ["A","D","E","E"]
word1 = "SEE"
word2 = "ABCB"
word3 = "ABCESEEE"
word4 = "aaa"

#print(Solution().exist(board, word1))
#print(Solution().exist(board, word2))
#print(Solution().exist(board2, word3))
print(Solution().exist(board3, word4))
