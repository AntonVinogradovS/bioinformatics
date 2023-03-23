def ManhattanTourist(n, m, down, right):
    s = [[0] * (m+1) for i in range(n+1)]
    for i in range(1,n+1):
        s[i][0] = s[i-1][0] + int(down[i-1][0])
    for j in range(1,m+1):
        s[0][j] = s[0][j-1] + int(right[0][j-1])
    for i in range(1,n+1):
        for j in range(1,m+1):
            s[i][j] = max(s[i-1][j] + int(down[i-1][j]), s[i][j-1] + int(right[i][j-1]))
    return s[n][m]



n, m = [int(x) for x in input().split()]
down = []
right = []
flag = 0
while (True):
    try:
        i=str(input()).replace(' ', '')
        if (i != '-')&(flag == 0):
            down.append(i)
        else:
            flag = 1
            if i != '-':
                right.append(i)
    except EOFError:
        break

res = ManhattanTourist(n,m,down,right)

print()