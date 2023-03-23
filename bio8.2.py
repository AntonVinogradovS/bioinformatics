#import sys

def GenomePathProblem(s):
	k = len(s[0])
	text = [s[0]]
	for i in range(1,len(s)):
		text.append(s[i][k-1]) ## the [-1] of the last element is "\n", [k-1] is safer.
	text = ''.join(text)
	return text


s = []
while True:
    try:
        s.append(input())
    except EOFError:
        break
print(s)