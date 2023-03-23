arrMass=[57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]

def ParentMass(Spectrum):
	return max(Spectrum)

def Mass(Peptid):
    return sum(Peptid)

def Expand(array): 
    res = []
    t = []
    for i in array:
        
        for j in arrMass:
            t = i.copy()
            t.append(j)
            res.append(t)
            
    return res


def cycSpec(peptide): #циклический пептид
    if len(peptide) == 1:
        return peptide
    spec = [0]
    for x in range(1,len(peptide)):
        for i in range(len(peptide)):
            if i+x >= len(peptide):
                y = i+x-len(peptide)
                spec.append(sum(peptide[i:])+sum(peptide[:y]))
            else:
                spec.append(sum(peptide[i:i+x]))
    spec.append(sum(peptide))
	#spec.sort()
    #print(spec)
    return spec



    #if len(peptide) == 1:
    #    return peptide
    #out_masses = [0]
##
    #m = 0
    #for s in peptide:
    #    out_masses.append(s)
    #    m += s
    #out_masses.append(m)
    #return out_masses

def Score(Peptide, spectrum):
    spec = cycSpec(Peptide)
    specTmp = spectrum.copy()
    score = 0
    i = 0
    for x in spec:
        if x in specTmp:
            specTmp.remove(x)
            score += 1
        #for y in range(i,len(spec)):
        #    if x == spec[y]:
        #        score +=1
        #        i = y+1
        #        break
    #print(score)
    return score
#def Score(Peptid,Spectrum):
#    print(Peptid)
#    Peptid1 = []
#    SpectrumNew = []
#    SpectrumNew.append(0)
#    for i in range(0,2):
#        for j in Peptid:
#            Peptid1.append(j)
#    for i in range(len(Peptid)):
#        for j in range(i+1, len(Peptid)):
#            SpectrumNew.append(sum(Peptid1[i:j]))
#    SpectrumNew.append(sum(Peptid))
#    SpectrumNew.sort()
#    SpectrumCopy = SpectrumNew.copy()
#    score = 0
#    for i in Spectrum:
#        if i in SpectrumCopy:
#            score += 1
#            SpectrumCopy.remove(i)
#    return score

def Trim(leaderBoard, Spectrum, count):
    res =[]
    if len(leaderBoard) <= count:
        return leaderBoard
    arrScore = []
    for i in leaderBoard:
        arrScore.append(Score(i, Spectrum))
    sortArrScore = arrScore.copy()
    sortArrScore.sort(reverse=True)
    check = sortArrScore[count-1]
    for i in range(len(leaderBoard)):
        if arrScore[i] >= check:
            res.append(leaderBoard[i])
    return res



count = int(input())
Spectrum = [int(x) for x in input().split(" ")]

leaderBoard = [[]]
leaderPeptide = []
lscore = 0
curr = 0
while leaderBoard != []:
    curr += 1
    #print(curr)
    leaderBoard = Expand(leaderBoard)
    #print(len(leaderBoard))
    immutable_peptides = leaderBoard[:]
    for Peptide in immutable_peptides:
        if Mass(Peptide) == ParentMass(Spectrum):
            if Score(Peptide, Spectrum) > Score(leaderPeptide, Spectrum):
                leaderPeptide = Peptide
        elif Mass(Peptide) > ParentMass(Spectrum):
            leaderBoard.remove(Peptide)
    #print(len(leaderBoard))     
    leaderBoard = Trim(leaderBoard, Spectrum, count)
    
print("-".join(map(str, leaderPeptide)))