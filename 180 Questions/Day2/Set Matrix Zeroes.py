matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
row = []
column = []
for i in range(0,len(matrix)):
    for j in range(0,len(matrix[i])):
        if matrix[i][j] == 0:
            row.append(i)
            column.append(j)
print(row)
print(column)
colsize = len(matrix)
rowsize = len(matrix[0])
for i in row:
    matrix[i] = [0 for i in range(rowsize)]
print(matrix)
for i in column:
    for j in range(len(matrix)):
        for k in range(rowsize):
            if k == i:
                matrix[j][k] = 0
print(matrix)
