
def CompositionProblem(inputStr, k):
    res = []
    res1 = []
    res2 = []
    for i in range(len(inputStr) - k + 1):
        res.append(inputStr[i:i+k])
        #print()
        res1.append(inputStr[i+1:k+i])
        res1.append((inputStr[i:i+k - 1 ]))
        #res1.append(inputStr[i:i+k-1])
    #res = list(set(res))
    res1 = list(set(res1))
   
    #print(sorted(res))
    return sorted(res), sorted(list(set(res1)))

def graphProblem(s, end, k):
    d = {}
    for i in s:
        d[i] = []
    for i in end:
        t = i[0:k-1]
        d[t].append(i[1:]) 
    for i in s:
        if d[i] == []:
            del d[i]

    #arr = []
    #i1 = -1
    #i2 = -1
    #leng = len(s[0])
    #for i in s:
    #    tmp = i
    #    i1 +=1
    #    for j in s:
    #        i2 +=1
    #        if i1 != i2:
    #            if i[1:] == j[:leng-1]:
    #                tmp2 = tmp + j[-1]
    #                if tmp2 in end:
    #                    arr.append(j)
    #    if len(arr) != 0:
    #        d[tmp] = arr
    #    arr = []
    #    i2 = -1
    return d   



    
    

# TCGGCCCATTTCTTTCCCGT
k = int(input())
inputStr = input()
res, res1 = CompositionProblem(inputStr, k)
#print(res1)

res2 = graphProblem(res1, res, k)
#print(res2)
for i in res2:
    if len(res2[i]) == 1:
        print(str(i) + ' -> ' + str(res2[i][0]))
    else:
        
        t = str(i) + ' -> ' + str(res2[i][0])
        for j in range(1, len(res2[i])):
            t += ',' + str(res2[i][j])
        print(t)