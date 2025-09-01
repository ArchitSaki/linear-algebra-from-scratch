import math
def cosine_similarity(v1, v2):
    
    v1_shape=v1.shape
    v2_shape=v2.shape
    if v1_shape==v2_shape:

    #dot product
        ans=0
        for i in range(len(v1)):
            ans=ans+v1[i]*v2[i]

    #magnitude
        mag_1=math.sqrt(sum(x**2 for x in v1))
        mag_2=math.sqrt(sum(x**2 for x in v2))
        

    #final
        result=ans/(mag_1*mag_2)
        return round(result,3)
