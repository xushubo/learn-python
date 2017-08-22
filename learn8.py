L = ['Bart', 'Lisa', 'Adam']
for x in L:
	print('hello,',x)


n = len(L)
m = 0
while(n>0):
	print('hello',L[m])
	n = n-1
	m = m+1
s = 1
while s<10:
	print (s,end='')#打印不换行 sep=''是不要打印空格 print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
	print(' ',end='')
	s = s+2
