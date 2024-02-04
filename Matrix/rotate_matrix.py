mat = [[1, 56, 3], [2, 2, 96], [4, 43, 5]]
print(mat)
# create a transpose of the matrix - 

for i in range(3):
    for j in range(i+1, 3):
        temp = mat[i][j]
        mat[i][j] = mat[j][i]
        mat[j][i] = temp

print("transpose matrix",mat)
for i in range(3):
    start = 0
    end = 2
    for j in range(3):
        temp1 = mat[start][i]
        mat[start][i] = mat[end][i]
        mat[end][i] = temp1
        start = start +  1
        end = end - 1
        if start >= end:
            break

print("Rotate Matrix by 90 degree clockwise - ", mat)        