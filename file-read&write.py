with open('C:/Users/DestoryBlue/Desktop/h.txt', 'r') as f:
	print(f.read())

with open('C:/Users/DestoryBlue/Desktop/h.txt', 'a') as f:
	f.write(' my name is Destroy')

from io import StringIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

d = StringIO('Hello!\nHi!\nGoodbye!')
while True:
	s = d.readline()
	if s is '':
		break
	print(s.strip())

from io import BytesIO
e = BytesIO()
e.write('中文'.encode('utf-8'))
print(e.getvalue())


b = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(b.read())

c = '   a f f   '
print(c.strip())