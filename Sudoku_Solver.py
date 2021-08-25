# https://www.youtube.com/playlist?list=PLzMcBGfZo4-kE3aF6Y0wNBNih7hWRAU2o
# https://www.youtube.com/watch?v=G_UYXzGuqvM

import pprint

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

    # box_x = pos[1] // 3
    # box_y = pos[0] // 3

    # for i in range(box_y*3, box_y*3 + 3):
    #     for j in range(box_x*3, box_x*3 + 3):
    #         if board[i][j] == num and (i,j) != pos:
    #             return False

    return True

def solve(board):
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
board = [
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

solvedBoard = [
        [5,3,4,6,7,8,9,1,2],
        [6,7,2,1,9,5,3,4,8],
        [1,9,8,3,4,2,5,6,7],
        [8,5,9,7,6,1,4,2,3],
        [4,2,6,8,5,3,7,9,1],
        [7,1,3,9,2,4,8,5,6],
        [9,6,1,5,3,7,2,8,4],
        [2,8,7,4,1,9,6,3,5],
        [3,4,5,2,8,6,1,7,9]
]

printBoard(board_2)
solve(board_2)
print('_____________________________________')
printBoard(board_2)
# print('_____________________________________')
# printBoard(solvedBoard)