import struct

print(struct.pack('>I', 10240099))
print(struct.unpack('>I', b'\x00\x9c@c'))
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))


def bmpinfo(file):
	with open(file, 'rb') as temp_f:
			temp_bmp = temp_f.read(30)
	bmp_tuple = struct.unpack('<ccIIIIIIHH', temp_bmp)
	if(bmp_tuple[0] == b'B' and bmp_tuple[1] == b'M'):
		print('this image file is bmp, size: %s*%s, colors: %s' % (bmp_tuple[6], bmp_tuple[7], bmp_tuple[9]))
	else:
		print('this image file is not bmp')

bmpinfo('C:\\Users\\DestoryBlue\\Desktop\\test.bmp')




