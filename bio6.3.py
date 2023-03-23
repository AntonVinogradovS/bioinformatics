
s1 = input()
s2 = input()
array = [["" for i in range(len(s2))] for i in range(len(s1))]
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] ==s2[j]:
            if j == 0 or i == 0:
                array[i][j] = s1[i]
            else:
                array[i][j] = array[i-1][j-1] + s1[i]
        else:
            len1 = len(array[i-1][j])
            len2 = len(array[i][j-1])
            if len1 > len2:
                array[i][j] = array[i-1][j]
            else:
                array[i][j] = array[i][j-1]
print(array)