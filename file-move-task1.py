import os
from datetime import *
print('当前时间：', datetime.today())
dir_file = input('请输入所查路径：')
print('文件名    ','大小    ','修改时间    ', '创建时间')
for x in os.listdir(dir_file):
	full_dir_file = os.path.join(dir_file, x)
	mod_time = os.path.getmtime(full_dir_file) #获取文件修改时间
	cha_time = os.path.getctime(full_dir_file) #获取文件创建时间
	mod_date = datetime.fromtimestamp(mod_time)
	cha_date = datetime.fromtimestamp(cha_time)
	print(x, os.path.getsize(full_dir_file), mod_date.strftime('%Y-%m-%d %H:%M:%S'), cha_date.strftime('%Y-%m-%d %H:%M:%S'))