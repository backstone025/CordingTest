matrix = [list(map(int, input().split())) for _ in range(9)]

max = max(max(row) for row in matrix)
row, column = next((i, row.index(max)) for i, row in enumerate(matrix) if max in row)

print(max)
print(f"{row + 1} {column + 1}")
