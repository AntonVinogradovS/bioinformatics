def kMerProblem(x, arr):
  
    t = 1
    for i in range(len(x)):
        curr = x[i]
        if curr == "A":
            
            t *= float(arr[0][i])
        elif curr  == "C":
            
            t *= float(arr[1][i])
        elif curr == "G":
            try:
                t *= float(arr[2][i])
            except IndexError:
                xx = float(arr[2][i])
                tt = t
                print(xx)
                print(tt)
        elif curr == "T":
            
            t *= float(arr[3][i])
    return t

def veryKMerProblem(Dna, k, array):
    maxEl = -1
    res = Dna[0:0+k]
    for i in range(len(Dna) + 1 - k):
        tmp = kMerProblem(Dna[i:i+k], array)
        if tmp > maxEl:
            maxEl = tmp
            res = Dna[i:i+k]
    return res



def Profile(M):
    k = len(M[0])
    res=[[0] * k for i in range(4)]
    for st in M:
        for i in range(len(st)):
            if st[i] == "A":
                res[0][i] += (1/len(M))
            if st[i] == "C":
                res[1][i] += (1/len(M))
            if st[i] == "G":
                res[2][i] += (1/len(M))
            if st[i] == "T":
                res[3][i] += (1/len(M))           
    return res          

def Score(arr):
    
    res = []
    
    for i in range(len(arr[0])):
        d = {"A": 0, "C":0,"G":0,"T":0}
        for j in range(len(arr)):
            d[arr[j][i]] += 1
        t = len(arr) - max(d.values())
        res.append(t)
    return sum(res)

def f():
    res = []
    for s in Dna:
        
        res.append(s[0:k])
    for i in range(len(Dna[0]) + 1 - k):
        M = []
        M.append(Dna[0][i:i+k])
        for j in range(1, t):
            profile = Profile(M)
            curr = veryKMerProblem(Dna[j], k, profile)
            M.append(curr)
        if Score(res) > Score(M):
            res = M
    return res


k, t = [int(x) for x in input().split()]
Dna = []
tmp = []

for i in range(t):
    Dna.append(str(input()))
res = f()
for i in res:
    print(i)
