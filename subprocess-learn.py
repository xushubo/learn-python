# -*- coding: utf-8 -*-
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
r1 = subprocess.call('nslookup www.python.org', shell=True) #使用了shell=True这个参数。这个时候，我们使用一整个字符串，而不是一个表来运行子进程。
print('Exit code:', r, r1)