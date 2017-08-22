import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))
print(s.recv(1024).decode('utf-8'))
# 接收欢迎消息:
'''
for data in [b'Michael', b'Tracy', b'Sarah']:
	# 发送数据:
	s.send(data)
	# 打印服务器返回的消息：
	print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
'''
while True:
	in_data = input('请输入对话内容：')
	s.send(in_data.encode('utf-8'))
	print(s.recv(1024).decode('utf-8'))
	if in_data == 'exit':
		break
s.close()