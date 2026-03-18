class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            mySet = set()
            for j in range(len(board[0])):
                if board[i][j] == '.': continue
                if board[i][j] in mySet : return False
                else : mySet.add(board[i][j])

        for i in range(len(board[0])):
            mySet = set()
            for j in range(len(board)):
                if board[j][i] == '.': continue
                if board[j][i] in mySet : return False
                else : mySet.add(board[j][i])
        
        for boxrow in range(0, 9, 3):
            for boxcol in range(0, 9, 3):
                mySet = set()
                for i in range(3):
                    for j in range(3):
                        val = board[boxrow+i][boxcol+j]
                        if val == '.': continue
                        if val in mySet: return False
                        mySet.add(val)

        return True