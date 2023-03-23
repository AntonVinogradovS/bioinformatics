def EditDistanceProblem(str1, str2, array):
    for i in range(1, len(str1) + 1):
        array[i][0] = i 
    for j in range(1, len(str2) + 1):
        array[0][j] = j
    for i in range(1, len(str1) + 1):
        for j in range (1, len(str2) + 1):
            if str1[i-1] == str2[j-1]:
                array[i][j] = M[i-1][j-1]
            else:
                x =array[i-1][j] +1
                y =array[i][j-1] + 1
                z = array[i-1][j-1] + 1
                array[i][j] = min(x, y, z)
    leng1 = len(str1)
    leng2 = len(str2)
    return(M[leng1][leng2])


str1 = str(input())
str2 = str(input())
M=[[]]
M = [[0 for j in range(len(str2) + 1)] for i in range(len(str1)+1)]
res = EditDistanceProblem(str1,str2,M)
print(res)
