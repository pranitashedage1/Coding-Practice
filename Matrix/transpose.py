# rows = 3
# cols = 3
# mat = [[0 for _ in range(rows)] for _ in range(cols)]
# print(mat)

mat = [[1, 56, 3], [2, 2, 96], [4, 43, 5]]
print(mat)
# create a transpose of the matrix - 

for i in range(3):
    for j in range(i+1, 3):
        temp = mat[i][j]
        mat[i][j] = mat[j][i]
        mat[j][i] = temp

print("transpose matrix",mat)