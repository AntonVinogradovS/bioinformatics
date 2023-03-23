
def allCombinations(Peptide1):
    tmp = [Peptide1]
    strTemp = ""
    for i in range(d):
        for Peptide in tmp:
            for j in range(k):
                if j == 0:
                    tmp.append("A" + Peptide[1:])
                    tmp.append("C" + Peptide[1:])
                    tmp.append("G" + Peptide[1:])
                    tmp.append("T" + Peptide[1:])
                    tmp = list(set(tmp))
                elif j != k:
                    strTemp = Peptide[:j] + "A" + Peptide[j+1:]
                    tmp.append(strTemp)
                    strTemp = ""
                    strTemp = Peptide[:j] + "C" + Peptide[j+1:]
                    tmp.append(strTemp)
                    strTemp = ""
                    strTemp = Peptide[:j] + "G" + Peptide[j+1:]
                    tmp.append(strTemp)
                    strTemp = ""
                    strTemp = Peptide[:j] + "T" + Peptide[j+1:]
                    tmp.append(strTemp)
                    strTemp = ""
                    tmp = list(set(tmp))
                else:
                    tmp.append(Peptide[:j] + "A")
                    tmp.append(Peptide[:j] + "C")
                    tmp.append(Peptide[:j] + "G")
                    tmp.append(Peptide[:j] + "T")
                    tmp = list(set(tmp))
    return tmp


k_d = [int(x) for x in input().split(" ")]
k = k_d[0]
d = k_d[1]

Dna = []
while True:
    try:
        Dna.append(input())
    except EOFError:
        break
#Dna = list()
#Dna = ['CACTGATCGACTTATC', 'CTCCGACTTACCCCAC', 'GTCTATCCCTGATGGC', 'CAGGGTTGTCTTGTCT']
count = 0

qwe = 0
res = []
for i in range(len(Dna)):
   for j in range(len(Dna[i])-k+1):
        PeptideArray = allCombinations(Dna[i][j:j+k])
        for pep in PeptideArray:
            approach = False
            qwe = 0
           # pep = "CTTA"
            for strCurr in range(len(Dna)):
                for t in range(len(Dna[strCurr])-k+1):
                    check = Dna[strCurr][t:t+k]
                    count = 0
                    for z in range(k):
                        if pep[z] != check[z]:
                            count += 1
                    if count <= d:
                        qwe += 1
                        break
                if qwe != strCurr + 1:
                    break
            if qwe == strCurr  + 1 :
                res.append(pep)

print(" ".join(map(str, set(res))))
            




#while(True):
#    s = input().strip()
#    if s == "":
#        break
#    Dna.append(s)
#for i in range(len(Dna)):
#    for j in range(len(Dna[i])-k+1):
#        allCombinations(Dna[i][j:j+k])
#print("111")
#while True:
#    try:
#        Dna.append(input())
#    except EOFError:
#        break

#tmp = 0
#res = []
#for i in range(len(Dna[0])-k+1):
#    approach = False
#    currElement = Dna[0][i:i+k]
#    for strCurr in range(1,len(Dna)):
#        for j in range(len(Dna[strCurr])-k+1):
#            checkElement = Dna[strCurr][j:j+k]
#            for m in range(k):
#                if checkElement[m] != currElement[m]:
#                    tmp += 1
#            if tmp <= d:
#                approach = True
#                break
#        if approach == False:
#            break 
#    if approach == True:
#        res.append(currElement)
#print(res)









