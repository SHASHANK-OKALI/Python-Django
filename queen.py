def is_safe(board,row,col):
    for i in range(row):
        if board[i] == col or abs(board[i]-col) == row - i:
            return False
    return True
    
def solve_n_queen(n):
    board = [-1]* n
    solutions=[]
    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board,row,col):
               board[row]=col
               backtrack(row+1)
               board[row]=-1
    backtrack(0)
    return solutions

sol = solve_n_queen(4)
print('Total solutions',len(sol))
for s in sol:
    print(s)