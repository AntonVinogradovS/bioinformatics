d = {}
d["G"] = 57
d["A"] = 71
d["S"] = 87
d["P"] = 97
d["V"] = 99
d["T"] = 101
d["C"] = 103
d["I"] = 113
d["L"] = 113
d["N"] = 114
d["D"] = 115
d["K"] = 128
d["Q"] = 128
d["E"] = 129
d["M"] = 131
d["H"] = 137
d["F"] = 147
d["R"] = 156
d["Y"] = 163
d["W"] = 186

str0 = input()
str1 = str0*2

res = []
res.append(0)
for i in range(len(str0)):
    for j in range(i + 1, i+len(str0)):
        tmp = str1[i: j]
        tmp2 = 0
        for x in tmp:
            tmp2 += d[x]
        res.append(tmp2)
        
tmp2 = 0
for i in str0:
    tmp2 += d[i]
res.append(tmp2)
res = sorted(res)
print (" ".join(map(str,res)))

        



