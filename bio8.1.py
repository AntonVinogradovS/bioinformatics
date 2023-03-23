k = int(input())
inputStr = input()
res = []
for i in range(len(inputStr) - k + 1):
    res.append(inputStr[i:i+k])
    print(inputStr[i:i+k])

