import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
'''
for data in [b'Michael', b'Trary', b'Sarah']:
	#发送数据
	s.sendto(data, ('127.0.0.1', 9999))
	#接收数据
	print(s.recv(1024).decode('utf-8'))
s.close()
'''

while True:
	in_data = input('请输入对话内容：')
	if in_data == 'exit':
		break
	s.sendto(in_data.encode('utf-8'), ('127.0.0.1', 9999))
	print(s.recv(1024).decode('utf-8'))
s.close()