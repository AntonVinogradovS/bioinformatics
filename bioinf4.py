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

inputStr = input()
res = ""
for i in range(0, len(inputStr), 3):
    if inputStr[i:i+3] in d and d[inputStr[i:i+3]] != "-":
        res += d[inputStr[i:i+3]]
print(res)
    
    
