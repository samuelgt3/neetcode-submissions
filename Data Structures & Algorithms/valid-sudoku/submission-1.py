class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen=[]
            for j in range(9):
                if board[i][j]=='.':
                    continue
                elif board[i][j] in seen:
                    print("h",seen,board[i][j])
                    return False
                else:
                    seen.append(board[i][j])
        for i in range(9):
            seen=[]
            for j in range(9):
                if board[j][i]=='.':
                    continue
                elif board[j][i] in seen:
                    print("v",seen,board[j][i])
                    return False
                else:
                    seen.append(board[j][i])

        rows=[[0,1,2],[3,4,5],[6,7,8]]
        for i in range(3):
            for j in range(3):
                seen=[]
                for x in rows[i]:
                    for y in rows[j]:
                        if board[x][y]=='.':
                            continue
                        elif board[x][y] in seen:
                            print(seen,board[x][y])
                            return False
                        else:
                            seen.append(board[x][y])
        return True