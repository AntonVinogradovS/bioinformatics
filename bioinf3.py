str = input()
res= ""
for x in str:
    if x == "A":
        res += "T"
    if x == "T":
        res += "A"
    if x == "G":
        res+= "C"
    if x == "C":
        res += "G"

print(res[::-1])