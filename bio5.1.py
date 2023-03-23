def kMerProblem(x, arr):
    t = 1
    for i in range(len(x)):
        curr = x[i]
        if curr == "A":
            
            t *= float(arr[0][i])
        elif curr  == "C":
            
            t *= float(arr[1][i])
        elif curr == "G":
            
            t *= float(arr[2][i])
        elif curr == "T":
            
            t *= float(arr[3][i])
    return t





Dna = str(input())
k = int(input())
Matrix = []
tmp = []
tmp=[x for x in input().split()]
Matrix.append(tmp)
tmp=[x for x in input().split()]
Matrix.append(tmp)
tmp=[x for x in input().split()]
Matrix.append(tmp)
tmp=[x for x in input().split()]
Matrix.append(tmp)
tmp = 0
maxEl = -1
res = ""
for i in range(len(Dna) + 1 - k):
    tmp = kMerProblem(Dna[i:i+k], Matrix)
    if tmp > maxEl:
        maxEl = tmp
        res = Dna[i:i+k]
print(res)




#print(Matrix)
