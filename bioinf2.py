str = input()
size = int(input())
d = {}
t  = 0
res = []
for i in range(len(str) - size + 1):
    if str[i:i+size] in d:
        d[str[i:i+size]] += 1
    else:
        d[str[i:i+size]] = 1

m = d[max(d, key = d.get)]
for i in d:
    
    if d[i] == m:
        res.append(i)


print(*res, sep=' ')




