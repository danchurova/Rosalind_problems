n = 7
k = 3
output = ''

s = range(0,n)

for i in s:
	if i == 0:
		s[0] = 1
	if i == 1:
		s[1] = 1
        if i >= 2:
		s[i] = s[i - 1] + k * s[i - 2]
		


print s[i] 
