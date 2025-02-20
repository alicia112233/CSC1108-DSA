def isValid(col, row, chessBoard):
    N = len(chessBoard)
    for r in range(row):
        if chessBoard[r][col] == 1:
            return False
        
    r = row - 1
    c = col - 1

    while r >= 0 and c >= 0:
        if chessBoard[r][c] == 1:
            return False
        r -= 1
        c -= 1

    r = row - 1
    c = col + 1

    while r >= 0 and c < N:
        if chessBoard[r][c] == 1:
            return False
        r -= 1
        c += 1
    
    return True

def printSolution(chessBoard):
    print("\n")
    for i in range(len(chessBoard)):
        print(chessBoard[i])

def putAQueen(row, chessBoard):
    N = len(chessBoard)
    for col in range(N):
        if isValid(col, row, chessBoard):
            chessBoard[row][col] = 1
            if (row < N-1):
                putAQueen(row + 1, chessBoard)
            else:
                printSolution(chessBoard)
                exit()
            chessBoard[row][col] = 0

N = 8
chessBoard = []
for i in range(N):
    chessBoard.append([])
    for j in range(N):
        chessBoard[i].append(0)

putAQueen(0, chessBoard)