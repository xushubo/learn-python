# -*- coding: GBK-*- #
import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('GBK'))
print('Exit code:', p.returncode)


print('$ cmd')
p1 = subprocess.Popen('cmd', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output1, err1 = p1.communicate(b'dir\ncd __py*\ndir\n')
print(output1.decode('GBK'))
print('Exit code:', p1.returncode)