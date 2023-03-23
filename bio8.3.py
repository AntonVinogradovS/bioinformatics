
def graphProblem(s):
    res = []
    tmp = ''
    leng = len(s[0])
    i1 = -1
    i2 = -1
    for i in s:
        i1 +=1
        for j in s:
            
            if i1 != i2:
                if i[1:] == j[:leng-1]:
                    tmp = str(i) + ' -> ' + str(j)
                    print(tmp)




s = []

s = [s for s in"""
ATGCG
GCATG
CATGC
AGGCA
GGCAT
""".split() if s]
#while True:
#    try:
#        s.append(input())
#    except EOFError:
#        break
graphProblem(s)

