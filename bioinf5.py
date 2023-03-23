
str = """AAA K
AAC N
AAG K
AAU N
ACA T
ACC T
ACG T
ACU T
AGA R
AGC S
AGG R
AGU S
AUA I
AUC I
AUG M
AUU I
CAA Q
CAC H
CAG Q
CAU H
CCA P
CCC P
CCG P
CCU P
CGA R
CGC R
CGG R
CGU R
CUA L
CUC L
CUG L
CUU L
GAA E
GAC D
GAG E
GAU D
GCA A
GCC A
GCG A
GCU A
GGA G
GGC G
GGG G
GGU G
GUA V
GUC V
GUG V
GUU V
UAA -
UAC Y
UAG -
UAU Y
UCA S
UCC S
UCG S
UCU S
UGA -
UGC C
UGG W
UGU C
UUA L
UUC F
UUG L
UUU F"""
arr = [x for x in str.split("\n")]

d = {}
for i in arr:
    d[i[0:3]] = i[4]

def check1(dnk, pep):
    dnkCopy = ""
    for i in dnk:
        if i == "T":
            dnkCopy += "U"
        else:
            dnkCopy += i
    t = -1
    for i in range(0, len(dnk), 3):
        t += 1
        if d[dnkCopy[i:i+3]] != pep[t]:
            return False 
    return True
        
    
def check2(dnk, pep):
    res = ""
    resEnd = ""
    for x in dnk:
        if x == "A":
            res += "T"
        elif x == "T":
            res += "A"
        elif x == "G":
            res+= "C"
        else:
            res += "G"
    for i in range(len(res)-1,-1, -1):
        resEnd += res[i]
    dnkCopy = ""
    for i in resEnd:
        if i == "T":
            dnkCopy += "U"
        else:
            dnkCopy += i
    t = -1
    for i in range(0, len(dnk), 3):
        t += 1
        if d[dnkCopy[i:i+3]] != pep[t]:
            return False 
    return True
    





DNK = input()
peptid = input()
flag = True
tmp = ""
for i in range(0, len(DNK)-3*len(peptid)+1):
    if check1(DNK[i:i+3*len(peptid)], peptid)  or check2(DNK[i:i+3*len(peptid)], peptid):
        print(DNK[i:i+3*len(peptid)])
