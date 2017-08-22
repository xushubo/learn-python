import re
test = '010-12345'
if re.match(r'^\d{3}-\d{3,8}$', test):
	print('ok')
else:
	print('failed')

print(re.split(r'\s+', 'a    b c'))
print(re.split(r'[\s\,]+', 'a,,b , c ,,, d'))
print(re.split(r'[\s\,\;]+', 'a,; b    c  ;;d'))

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m)
print(m.group(0), m.group(1), m.group(2))
print(type(m.group(1)))
print(m.groups())

t = '19:05:30'
n = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9]):(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9]):(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(n.groups())

print(re.match(r'^(\d+)(0*)$', '102300'))
print(re.match(r'^(\d+)(0*)$', '102300').groups)
print(re.match(r'^(\d+)(0*)$', '102300').groups())

print(re.match(r'^(\d+?)(0*)$', '102300').groups())

#如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：
#编译：
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('020-10086').groups())

re_email = re.compile(r'^[a-zA-Z]+[.]?[a-zA-Z0-9]*@[a-z0-9]+[.][a-z]+$')
print(re_email.match('someone@gmail.com'))
print(re_email.match('bill.gates@microsoft.com'))

re_email1 = re.compile(r'^<([A-Z][a-z]+\s?[A-Z][a-z]+)>\s[0-9a-zA-Z]+@[0-9a-zA-Z]+[.][a-z]+$')
print(re_email1.match('<Tom Paris> tom@voyager.org'))
print(re_email1.match('<Michael Jackson> tom@voyager.com'))
print(re_email1.match('<Tom Paris> tom@voyager.org').group(1))
print(re_email1.match('<Michael Jackson> tom@voyager.org').group(1))

str_pattern = '中国|美国|韩国'

pattern = re.compile(str_pattern)

str_to_match = '我是中国人'

m = pattern.search(str_to_match)

if m:
	print(str_to_match[m.start(): m.end()])