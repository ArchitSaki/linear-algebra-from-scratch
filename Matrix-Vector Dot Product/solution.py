def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	a_len=len(a[0])
	b_len=len(b)
	if a_len != b_len:
		return -1
	output=[]
	
	for row in a:
		ans=0
		for j in range (len(b)):
			ans=ans+row[j]*b[j]
		output.append(ans)

	return output
