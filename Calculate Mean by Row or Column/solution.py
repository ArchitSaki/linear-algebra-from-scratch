def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    result=[]
    if mode == "row":
        for row in matrix:
            result.append(sum(row) / len(row))
    elif mode == "column":
        num_cols = len(matrix[0])
        for i in range(num_cols):
            col_sum=0
            for j in range(len(matrix)):
                col_sum += matrix[j][i]
            result.append(col_sum / len(matrix))
    else:
        pass
    
    return result
