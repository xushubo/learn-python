from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

def rndChar():
	return chr(random.choice([x for x in range(48, 123) if x not in [y for y in range(58, 65)] and x not in [z for z in range(91, 97)]]))

def rndColor():
	return (random.randint(128, 255), random.randint(128, 255), random.randint(128, 255))

def rndColor2():
	return (random.randint(64, 127), random.randint(64, 127), random.randint(64, 127))

#返回一个随机tuple
def rndline():
	return (random.random()*240, random.random()*60 ,random.random()*240, random.random()*60)
#返回随机大小的字体
def rndfont():
	return ImageFont.truetype('C:\\Windows\\Fonts\\Arial.ttf', random.randint(20, 40))

width = 60 * 4
height = 60
#创建图片，尺寸240x60，颜色模式RGB，填充色纯白色
image = Image.new('RGB', (width, height), (255, 255, 255))
# font = ImageFont.truetype('C:\\Windows\\Fonts\\Arial.ttf', random.randint(25, 36))
#新建一个画板实例，传入参数刚刚创建的img对象作为画板
draw = ImageDraw.Draw(image)
for x in range(width):
	for y in range(height):
		draw.point((x, y), fill=rndColor())

for i in range(4):
	# 新建一个透明图片img
	image_temp = Image.new('RGBA', (55, 55), (255, 255, 255, 0))
	# img作为画板
	image_temp_draw = ImageDraw.Draw(image_temp)
	# 画板写字
	image_temp_draw.text((15, 8), rndChar(), font=rndfont(), fill=rndColor2())
	# 画板旋转
	image_temp = image_temp.rotate(random.randint(-45, 45))
	#把image_temp粘贴到image上面
	image.paste(image_temp, (60 * i + 10, 10), mask=image_temp)

draw.line(rndline(), rndColor2()) #画随机线
draw.line(rndline(), rndColor2())
draw.line(rndline(), rndColor2())
draw.line(rndline(), rndColor2())
#预览img
image.show()