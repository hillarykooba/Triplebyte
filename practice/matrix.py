'''
The bug here is that "matrix" contains two references to the same object, so a change to one row shows up in both rows. The programmer likely wanted references to two different objects. The solution here is to append a copy of row to matrix, with something like matrix.append(copy.copy(row)). More compactly in Python, a 2D array can be initialized with matrix = [[0 for _ in range(width)] for _ in range(height)].
'''

matrix = []
row = [0, 0]
for i in range(2):
    matrix.append(row)
matrix[1][1] = 1
print matrix

# Output [[0, 1], [0, 1]]
