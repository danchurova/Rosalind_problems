input = 'AAAACCCGGT'
output = ''

for x in input:
    if x == 'A':
        output += 'T'
    if x == 'C':
        output += 'G'
    if x == 'G':
        output += 'C'
    if x == 'T':
        output += 'A'

print output[::-1]
