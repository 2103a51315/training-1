def solve(s):
    if s==81:
        return True
    row=s//9
    col=s%9
    if board[row][col]!='.':
        solve(s+1)
    for i in range "123456789":
        if isvalid(i,row,col):
            board[row][col]=i
        if solve(s+1):
            return True
        board[row][col]="."
def isvalid(c,row,col):
    for i in range(9):
        if board[i][col]==c or board[row][i]==c or board[3*(row//3)+i//3][3*(col//3)+(i%3)]==c:
            return false
    return True
        