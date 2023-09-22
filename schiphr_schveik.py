page = input('page: ')
schiphr = input('numbers: ')
ans = ''
for x in schiphr.split(' '):
    ans += ' ' + page.split(' ')[int(x)]
print(ans)
