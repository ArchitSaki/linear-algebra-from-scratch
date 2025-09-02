from typing import List
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    a_len=len(a)
    b_len=len(b[0])
    if len(a[0])!=len(b):
        raise ValueError("check Matrix shape!")
    
    output=[[0 for _ in range(len(b[0]))] for _ in range(len(a))]
	
    for i in range(len(a)):
        
        for j in  range(len(b[0])):
            
            sum=0
            for k in range(len(a[0])):
                sum+=a[i][k]*b[k][j]
            output[i][j]=sum
    return output
                
