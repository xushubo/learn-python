#枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。Python提供了Enum类来实现这个功能：
from enum import Enum, unique
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'sep', 'Oct','Nov', 'Dec'))
print(Month.Jan)
print(Month.Jan.value)

for name, member in Month.__members__.items():
	print(name, '=>', member, ',', member.value)
#value属性则是自动赋给成员的int常量，默认从1开始计数。

#如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：

@unique   #@unique装饰器可以帮助我们检查保证没有重复值。
#如果要限制定义枚举时，不能定义相同值的成员。可以使用装饰器@unique
class Weekday(Enum): #定义枚举时，成员名称不允许重复
	Sun = 0
#	Sdd = 1   # 默认情况下，不同的成员值允许相同。但是两个相同值的成员，第二个成员的名称被视作第一个成员的别名
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6

#枚举支持迭代器，可以遍历枚举成员
for week in Weekday:  #如果枚举有值重复的成员，循环遍历枚举时只获取值重复成员的第一个成员
	print(week)

#如果想把值重复的成员也遍历出来，要用枚举的一个特殊属性__members__
for name, member in Weekday.__members__.items():
	print(name, '=>', member, ',', member.value)

day1 = Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Tue']) #通过成员的名称来获取成员
print(Weekday.Tue.value)
print(day1 == Weekday.Mon)
print(day1 == Weekday.Tue)
print(Weekday(1))  #通过成员值来获取成员,如果枚举中存在相同值的成员，在通过值获取枚举成员时，只能获取到第一个成员
print(day1 == Weekday(1))
print(day1.name)  #通过成员，来获取它的名称和值
print(day1.value)
print(Weekday.Mon is Weekday.Mon)
print(Weekday.Mon is not Weekday.Sun)
#枚举成员不能进行大小比较
#Weekday.Mon > Weekday.Sun