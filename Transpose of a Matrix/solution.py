def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	col=len(a[0])
    row=len(a)
    out=[[0]*row for v in range(col)]

    for i in range(row):
        for j in range(col):
            out[j][i] = a[i][j]
    
    return out
