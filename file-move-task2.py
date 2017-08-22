import os

full_file_dir = os.path.abspath('.')

for x in os.listdir('.'):
	dir_list = []
	if os.path.isfile(os.path.join(full_file_dir, x)) and x.count('learn'):
		print('相对路径：', os.path.split(full_file_dir)[1], x)
	else:
		dir_list.append(x)

for n in dir_list:
	file_dir = os.path.join(full_file_dir, n)
	for x in os.listdir(file_dir):
		if os.path.isfile(os.path.join(file_dir, x)) and x.count('learn'):
			print('相对路径：', os.path.join(os.path.split(full_file_dir)[1], n), x)