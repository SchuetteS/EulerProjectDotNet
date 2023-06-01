def printBoard(board):
    for row in range(len(board)):
        
        if row % 3 == 0:
            print('- - - - - - - - - - - -')
        
        for col in range(len(board[row])):
            if col % 3 == 0:
                print('|', end = ' ')
            if col == 8:
                print(board[row][col])
            else:
                print(board[row][col], end = ' ')

def findEmpty(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                return(row, col)
    return None

def isValid(board, num, pos):
    # check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # check  square
    row = pos[0] - pos[0] % 3
    col = pos[1] - pos[1] % 3
    
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(board):
    global solve_counter
    solve_counter += 1

    find = findEmpty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if isValid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False



# https://de.wikipedia.org/wiki/Sudoku
# 10845902 Aufrufe von Solve() zur Lösung

board_1 = [
    [0,3,0,0,0,0,0,0,0],
    [0,0,0,1,9,5,0,0,0],
    [0,0,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,0],
    [4,0,0,8,0,0,0,0,1],
    [0,0,0,0,2,0,0,0,0],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,0,0,0,7,0]
]

# 92 Aufrufe von Solve() zur Lösung
board_2 = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

board_3 = [
    [6,9,0,0,0,0,5,7,0],
    [4,0,0,7,0,6,0,0,0],
    [7,1,0,0,0,0,3,0,0],
    [8,0,0,4,0,0,6,0,0],
    [0,0,0,3,5,2,0,0,0],
    [0,0,9,0,0,8,0,0,1],
    [0,0,1,0,0,0,0,8,7],
    [0,0,0,9,0,3,0,0,4],
    [0,8,4,0,0,0,0,6,3]
]

board_4 = [
    [0,0,4,3,0,0,0,9,6],
    [0,0,7,9,0,0,0,0,0],
    [0,0,9,0,0,4,0,3,5],
    [8,0,0,0,0,7,0,0,0],
    [5,9,0,0,8,0,0,7,4],
    [0,0,0,4,0,0,0,0,2],
    [4,2,0,5,0,0,6,0,0],
    [0,0,0,0,0,8,2,0,0],
    [1,7,0,0,0,3,5,0,0]
]

solve_counter = 0
board = board_4

printBoard(board)
solve(board)
print('_____________________________________')
printBoard(board)
print(solve_counter)
