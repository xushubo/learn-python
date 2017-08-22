from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import Counter

#namedtuple是一个函数，它用来创建一个自定义的tuple对象，
#并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

print(isinstance(p, Point))
print(isinstance(p, tuple))

rectangle_cube = namedtuple('rectangle_cube', ['x', 'y', 'z'])
r = rectangle_cube(4, 3, 6)
print(r.x, r.y, r.z)

#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
q = deque(['x', 'y', 'z'])
q.append('a')
q.appendleft('b')
print(q)
print(isinstance(q, deque))
print(isinstance(q, list))
q.pop()
print(q)
q.popleft()
print(q)

#使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
dd = defaultdict(lambda: 'N/A') #注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])
print(isinstance(dd, defaultdict))
print(isinstance(dd, dict))

d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d) # dict的Key是无序的
#如果要保持Key的顺序，可以用OrderedDict：
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)
print(isinstance(od, dict))
#注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
od1 = OrderedDict()
od1['z'] = 1
od1['x'] = 2
od1['y'] = 3
print(od1)
print(list(od1.keys()))

#Counter是一个简单的计数器，例如，统计字符出现的个数：
c = Counter()
for ch in 'programming':
	c[ch] = c[ch] + 1
print(c)

print(isinstance(c, Counter))
print(isinstance(c, dict))