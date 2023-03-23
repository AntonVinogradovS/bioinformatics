array = ["A","C","G","T"]
def allCombinations(k):
    tempArray = array.copy()
    for i in range(k-1):
        currArray = []
        for j in tempArray:
            for z in array:
                currArray.append(j+z)
        tempArray = currArray
    return tempArray

def hammingDist(combination, Str):
    distance = len(combination)
    k = len(combination)
    m = len(Str)

    for i in range(m - k + 1):
        tmp = 0
        cut = Str[i:i+k]
        for j in range(k):
            if combination[j] != cut[j]:
                tmp += 1
        if  distance > tmp:
            distance = tmp
    return distance



n = int(input())
Dna = []
while True:
    try:
        Dna.append(input())
    except EOFError:
        break

Combinations = allCombinations(n)


res = 0

tmp = ()
minDist = len(Dna[0]) + 1

for combination in Combinations:
    count = 0
    for j in range(len(Dna)):
        currStr = Dna[j]
        count += hammingDist(combination, currStr)
    if minDist > count:
        minDist = count
        res = combination
print(res)
        
    


