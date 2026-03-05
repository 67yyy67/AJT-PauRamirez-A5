mat = [
    [1, 1, 1, 6],
    [2, -1, 1, 3],
    [1, 2, -1, 3]
]



for i in range(len(mat)):
    for i2 in range(len(mat)):
            if i2 == i:
                pass
            else:
                div = (mat[i2][i]/mat[i][i])
                for j2 in range(len(mat[i2])):
                    mat[i2][j2] = mat[i2][j2] - mat[i][j2]*div
print(mat)