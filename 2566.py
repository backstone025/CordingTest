matrix = []
row, column = 0, 0

for _ in range(9):
    matrix.append([int(x) for x in map(int, input().split())])

max = 0
for i in range(9):
    for j in range(9):
        if matrix[i][j] >= max:
            max = matrix[i][j]
            row = i
            column = j

        else:
            continue

print(max)
print("{0} {1}".format(row + 1, column + 1))

