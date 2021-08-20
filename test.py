grid = [
        ['1a', '1b', '1c', '1d', '1e'],
        ['2a', '2b', '2c', '2d', '2e'],
        ['3a', '3b', '3c', '3d', '3e'],
        ['4a', '4b', '4c', '4d', '4e'],
        ['5a', '5b', '5c', '5d', '5e']
        ]

for row in range(len(grid)):
    print('\n')
    for column in range(len(grid[row])):
        print(grid[row][column], end = ' ')

print('\n\n--------------')

for column in range(len(grid[row])):
    print('\n')
    for row in range(len(grid)):
        print(grid[row][column], end = ' ')

print('\n\n--------------')

# 1b = 1 2
# 2c = 2 3
# 3d = 3 4
for row in range(len(grid) - 3):
    print('\n')

    for column in range(len(grid[row]) - 3):

        print(grid[row][column], end = ' ')

        for i in range(1, 4):
            print(grid[row + i][column + i], end = ' ')
            
print('\n\n--------------')
# 1e = 1 5
# 2d = 2 4
# 3c = 3 3
for row in range(len(grid) - 3):
    for column in grid[row][::-1]: 

        print(column)
        print(grid[row][column], end = ' ')

        for i in range(1, 4):
            print(grid[row + i][column + i], end = ' ')