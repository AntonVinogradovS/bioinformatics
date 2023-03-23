arrMass=[57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]


def ParentMass(Spectrum):
	return max(Spectrum)

def Mass(Peptid):
    return sum(Peptid)



def Expand(Peptides,Spectrum): # Большой вопрос. Стоит проверить
    PeptidesNew = []
    t = []
    for i in Peptides:
        for j in arrMass:
            if j in Spectrum:
                t = i.copy()
                t.append(j)
                PeptidesNew.append(t)
                t = []
    return PeptidesNew

def Consistent(Peptid, Spectrum):
    if Peptid==0: 
        return False
    PeptidNew = []
    for i in range(len(Peptid)):
        for j in range(1,len(Peptid)):
            if i+j <= len(Peptid):
                PeptidNew.append(sum(Peptid[i:i+j]))          
    PeptidNew.sort()
    SpectrumCopy=Spectrum.copy()

    for i in PeptidNew:
        if i in SpectrumCopy:
            SpectrumCopy.remove(i)
            if Mass(Peptid) not in SpectrumCopy:
                return False
        else:
            return False      
    return True

def Cyclospectrum(Peptid0,Spectrum):
    if Peptid0 == 0:
        return False
    Peptid1 = []
    res = []
    res.append(0)
    for i in range(0,2):
        for j in Peptid0:
            Peptid1.append(j)
    for i in range(len(Peptid0)):
        for j in range(i+1, i + len(Peptid0)):
            res.append(sum(Peptid1[i:j]))
    res.append(sum(Peptid0))
    res.sort()
    if len(res) == len(Spectrum):
        if res[i] != Spectrum[i]:
            return False
    return True
    
    
Spectrum = [int(x) for x in input().split()]
Peptides = [[]]
for i in Spectrum:
    if i in arrMass:
        Peptides.append(i)

t = []
PeptidesNew = []
for i in Peptides:
    for j in arrMass:
        t.append(i)
        t.append(j)
        PeptidesNew.append(t)
        t = []
Peptides = PeptidesNew

#print(len(Peptides))


for i in range(len(Peptides)-1,-1,-1):
    PeptidTemp = Peptides[i]
    if PeptidTemp == 0:
        Peptides.remove(PeptidTemp)
        continue
    SpectrumCopy = Spectrum.copy()
    for j in PeptidTemp:
        if j in SpectrumCopy:
            SpectrumCopy.remove(j)
            if Mass(PeptidTemp) not in SpectrumCopy:
                Peptides.remove(PeptidTemp)
                break
        else:
            Peptides.remove(PeptidTemp)
            break
        #if Mass(PeptidTemp) not in SpectrumCopy:
             #Peptides.remove(PeptidTemp)

checkArr = [[]]
while (len(Peptides) != 0):
    Peptides = Expand(Peptides,Spectrum)
    for i in range(len(Peptides)-1, -1, -1):
        if (ParentMass(Spectrum) == Mass(Peptides[i])):
            if(Cyclospectrum(Peptides[i], Spectrum)):
                if Peptides[i] not in checkArr:
                    checkArr.append(Peptides[i])
                    print('-'.join(map(str,Peptides[i])))
            Peptides.remove(Peptides[i])
        elif Consistent(Peptides[i],Spectrum) != True:
            Peptides.remove(Peptides[i])

