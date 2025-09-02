def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]):
	a, b = matrix[0]
    c, d = matrix[1]

    det=a*d-b*c
    abc=a+d
    
    discriminant = math.sqrt(abc**2 - 4*det)
    lambda1 = (abc + discriminant) / 2
    lambda2 = (abc - discriminant) / 2
