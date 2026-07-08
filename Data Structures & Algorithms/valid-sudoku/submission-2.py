import numpy as np
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        lst = board
        #print(np.array(lst).shape)
        #comparing the rows
        for i in range(9):
            mydict_r = {}
            mydict_c = {}
            for j in range(9):
                #print(f"board[{i}][{j}]" ,board[i][j])
                if board[i][j] == ".": pass
                elif( 1 <= int(board[i][j]) <=9):
                    if mydict_r.get(board[i][j]) is not None:
                        return False
                    else:
                        mydict_r[board[i][j]] = 1

                if board[j][i] == ".": pass
                elif( 1 <= int(board[j][i]) <=9):
                    if mydict_c.get(board[j][i]) is not None:
                        return False
                    else:
                        mydict_c[board[j][i]] = 1
                #print("mydict",mydict)
    
        boxes_seen = [[0] * 9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                sub_idx = ((i//3)*3) + (j//3)
                if board[i][j] == ".": pass
                elif(boxes_seen[sub_idx][int(board[i][j]) -1] == 1):
                    return False
                else:
                    boxes_seen[sub_idx][int(board[i][j])-1] = 1
        return True
            
