from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
'''
# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('IMG_1618.JPG')
# 获得图像尺寸:
width, height = im.size
print('Original image size: %sx%s' % (width, height))
# 缩放到50%:
im.thumbnail((width//2, height//2))
print('Resize image to: %sx%s' % (width//2, height//2))
# 把缩放后的图像用jpeg格式保存:
im.save('thumnail.jpg', 'jpeg')

# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')

#应用轮廓滤镜:
im2 = im.filter(ImageFilter.CONTOUR)
im2.save('CONTOUR.jpg', 'jpeg')

#应用细节增强滤镜:
im2 = im.filter(ImageFilter.DETAIL)
im2.save('DETAIL.jpg', 'jpeg')

#应用边缘增强滤镜:突出、加强和改善图像中不同灰度区域之间的边界和轮廓的图像增强方法。
#经处理使得边界和边缘在图像上表现为图像灰度的突变,用以提高人眼识别能力。
im2 = im.filter(ImageFilter.EDGE_ENHANCE)
im2.save('EDGE_ENHANCE.jpg', 'jpeg')

#应用深度边缘增强滤镜，会使得图像中边缘部分更加明显
im2 = im.filter(ImageFilter.EDGE_ENHANCE_MORE)
im2.save('EDGE_ENHANCE_MORE.jpg', 'jpeg')

#应用浮雕滤镜
im2 = im.filter(ImageFilter.EMBOSS)
im2.save('EMBOSS.jpg', 'jpeg')

#应用寻找边缘信息滤镜
im2 = im.filter(ImageFilter.FIND_EDGES)
im2.save('FIND_EDGES.jpg', 'jpeg')

#应用平滑滤镜，突出图像的宽大区域、低频成分、主干部分或抑制图像噪声和干扰高频成分，使图像亮度平缓渐变，减小突变梯度，改善图像质量。
im2 = im.filter(ImageFilter.SMOOTH)
im2.save('SMOOTH.jpg', 'jpeg')

#应用深度平滑滤镜，会使得图像变得更加平滑。
im2 = im.filter(ImageFilter.SMOOTH_MORE)
im2.save('SMOOTH_MORE.jpg', 'jpeg')

#应用锐化滤波，补偿图像的轮廓，增强图像的边缘及灰度跳变的部分，使图像变得清晰
im2 = im.filter(ImageFilter.SHARPEN)
im2.save('SHARPEN.jpg', 'jpeg')
'''
#随机大小写字母以及数字： 
def rndChar():
	return chr(random.choice([x for x in range(48, 123) if x not in [y for y in range(58, 65)] and x not in [z for z in range(91, 97)]]))

#随机颜色1：
def rndColor():
	return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

#随机颜色2：
def rndColor2():
	return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

#240 x 60
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
#创建Font对象：
font = ImageFont.truetype('C:\\Windows\\Fonts\\Arial.ttf', 36)
#创建Draw对象：
draw = ImageDraw.Draw(image)
#填充每个像素：
for x in range(width):
	for y in range(height):
		draw.point((x, y), fill=rndColor())
#输出文字：
for t in range(4):
	draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
#模糊：
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')