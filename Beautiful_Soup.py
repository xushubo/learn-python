import re
import bs4
#from bs4 import BeautifulSoup
html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
#创建 beautifulsoup 对象
soup = bs4.BeautifulSoup(html,'lxml')
#print(soup.prettify())    #打印一下 soup 对象的内容
#Tag 是什么？通俗点讲就是 HTML 中的一个个标签 用 Beautiful Soup 来方便地获取 Tags
print(soup.title)
print(soup.head)
print(soup.p)
print(soup.a)
print(type(soup.a))
print(type(soup.p))

#对于 Tag，它有两个重要的属性，是 name 和 attrs
print(soup.name) #soup 对象本身比较特殊，它的 name 即为 [document]，对于其他内部标签，输出的值便为标签本身的名称。
print(soup.head.name)
print(soup.p.attrs)

#如果我们想要单独获取某个属性，可以这样，例如我们获取它的 class 叫什么
print(soup.p['class'])

#利用get方法，传入属性的名称
print(soup.p.get('class'))

#可以对这些属性和内容等等进行修改
soup.p['class'] = 'newclass'
print(soup.p)

#还可以对这个属性进行删除
#del soup.p['class']
#print(soup.p)
#print(html)

#获取标签内部的文字,用 .string 即可
print(soup.p.string)
print(type(soup.p.string))

#BeautifulSoup 对象表示的是一个文档的全部内容.
#大部分时候,可以把它当作 Tag 对象，是一个特殊的 Tag，我们可以分别获取它的类型，名称
print(type(soup.name))
print(soup.name)
print(soup.attrs)

#Comment 对象是一个特殊类型的 NavigableString 对象，其实输出的内容仍然不包括注释符号
print(soup.a)
print(soup.a.string)
print(type(soup.a.string))

#a 标签里的内容实际上是注释，但是如果我们利用 .string 来输出它的内容，
#我们发现它已经把注释符号去掉了，所以这可能会给我们带来不必要的麻烦。
#另外我们打印输出下它的类型，发现它是一个 Comment 类型，所以，我们在使用前最好做一下判断
if isinstance(soup.a.string, bs4.element.Comment):
	print(soup.a.string)

#遍历文档树 直接子节点 要点：.contents  .children  属性
#tag 的 .content 属性可以将tag的子节点以列表的方式输出
print(soup.body.contents)
print(len(soup.body.contents))
print(type(soup.body.contents))

#输出方式为列表，我们可以用列表索引来获取它的某一个元素
print(soup.body.contents[0])
print(type(soup.body.contents[0]))

#.children 它返回的不是一个 list，不过我们可以通过遍历获取所有子节点。
#我们打印输出 .children 看一下，可以发现它是一个 list 生成器对象
print(soup.body.children)
print(type(soup.body.children))
for children in soup.body.children:
	print(children)
print('-------------------------')
#所有子孙节点 知识点：.descendants 属性
#.contents 和 .children 属性仅包含tag的直接子节点，
#.descendants 属性可以对所有tag的子孙节点进行递归循环，和 children类似，我们也需要遍历获取其中的内容。
for children in soup.descendants:
	print(children)

#如果tag只有一个 NavigableString 类型子节点,那么这个tag可以使用 .string 得到子节点。
#如果一个tag仅有一个子节点,那么这个tag也可以使用 .string 方法,输出结果与当前唯一子节点的 .string 结果相同。
print(soup.head.string)
print(soup.title.string)

#如果tag包含了多个子节点,tag就无法确定，string 方法应该调用哪个子节点的内容, .string 的输出结果是 None
print(soup.html.string)

#知识点： .strings  .stripped_strings 属性
#.strings获取多个内容，不过需要遍历获取，比如下面的例子
for string in soup.strings:
	print(repr(string))

#.stripped_strings 输出的字符串中可能包含了很多空格或空行,使用 .stripped_strings 可以去除多余空白内容
for string in soup.stripped_strings:
	print(repr(string))

#父节点 知识点： .parent 属性
print(soup.p.parent.name)
print(soup.head.parent.name)
content = soup.head.title.string
print(content.parent.name)

#全部父节点 知识点：.parents 属性 通过元素的 .parents 属性可以递归得到元素的所有父辈节点
for parent in content.parents:
	print(parent.name)

#兄弟节点可以理解为和本节点处在同一级的节点，
#.next_sibling 属性获取了该节点的下一个兄弟节点，.prev_sibling 则与之相反，如果节点不存在，则返回 None
#实际文档中的tag的 .next_sibling 和 .prev_sibling 属性通常是字符串或空白，
#因为空白或者换行也可以被视作一个节点，所以得到的结果可能是空白或者换行
print(soup.head.next_sibling)
print(soup.head.next_sibling.next_sibling)
print(soup.head.next_sibling.next_sibling.next_sibling)
print(soup.p.prev_sibling)
print(soup.p.next_sibling)

#全部兄弟节点 通过 .next_siblings 和 .previous_siblings 属性可以对当前节点的兄弟节点迭代输出

for sibling in soup.a.next_siblings:
	print(repr(sibling))
	print(sibling.name)

print(soup.a.prev_siblings)
print('-----------------')

#前后节点.next_element  .previous_element 属性 与 .next_sibling  .previous_sibling 不同，
#它并不是针对于兄弟节点，而是在所有节点，不分层次
#比如 head 节点为<head><title>The Dormouse's story</title></head> 那么它的下一个节点便是 title，它是不分层次关系的
print(soup.head.next_element)
print('--------------------')

#所有前后节点 通过 .next_elements 和 .previous_elements 的迭代器就可以向前或向后访问文档的解析内容,就好像文档正在被解析一样
for element in soup.p.next_elements:
	print(repr(element))
	print('======')

print(soup.title.previous_element)

#搜索文档树 find_all( name , attrs , recursive , text , **kwargs )
#find_all() 方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件
#name 参数可以查找所有名字为 name 的tag,字符串对象会被自动忽略掉
#传字符串 Beautiful Soup会查找与字符串完整匹配的内容
print(soup.find_all('b'))
print(soup.find_all('a'))

#传正则表达式 Beautiful Soup会通过正则表达式的 match() 来匹配内容
for tag in soup.find_all(re.compile(r'^b')):    #找出所有以b开头的标签
	print(tag.name)

#传列表 Beautiful Soup会将与列表中任一元素匹配的内容返回
print(soup.find_all(['a', 'b']))

#传 True 可以匹配任何值,下面代码查找到所有的tag,但是不会返回字符串节点
for tag in soup.find_all(True):
	print(tag.name)

#传方法 如果没有合适过滤器,那么还可以定义一个方法,方法只接受一个元素参数
#如果这个方法返回 True 表示当前元素匹配并且被找到,如果不是则反回 False
#下面方法校验了当前元素,如果包含 class 属性却不包含 id 属性,那么将返回 True:

def has_class_but_no_id(tag):
	return tag.has_attr('class') and not tag.has_attr('id')

print(soup.find_all(has_class_but_no_id))

#keyword 参数 
#如果包含一个名字为 id 的参数,Beautiful Soup会搜索每个tag的”id”属性
print(soup.find_all(id='link2'))
#如果传入 href 参数,Beautiful Soup会搜索每个tag的”href”属性
print(soup.find_all(href=re.compile('elsie')))
print(soup.find_all(href=re.compile('elsie'), id='link1'))

#在这里我们想用 class 过滤，不过 class 是 python 的关键词，这怎么办？加个下划线就可以
print(soup.find_all('a', class_='sister', id='link3'))

#有些tag属性在搜索不能使用,比如HTML5中的 data-* 属性
#data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
#data_soup.find_all(data-foo="value")
#SyntaxError: keyword can't be an expression

#但是可以通过 find_all() 方法的 attrs 参数定义一个字典参数来搜索包含特殊属性的tag
data_soup = bs4.BeautifulSoup('<div data-foo="value">foo!</div>', 'lxml')
print(data_soup.find_all(attrs={'data-foo':'value'}))

#text 参数 通过 text 参数可以搜搜文档中的字符串内容.
#与 name 参数的可选值一样, text 参数接受 字符串 , 正则表达式 , 列表, Tru
print(soup.find_all(text='Lacie'))
print(soup.find_all(text=['Tillie', ' Elsie ', 'Lacie']))
print(soup.find_all(text=re.compile('^The')))

#limit 参数 find_all() 方法返回全部的搜索结构,如果文档树很大那么搜索会很慢.
#如果我们不需要全部结果,可以使用 limit 参数限制返回结果的数量.
print(soup.find_all('a', limit=2))

#recursive 参数 调用tag的 find_all() 方法时,Beautiful Soup会检索当前tag的所有子孙节点,
#如果只想搜索tag的直接子节点,可以使用参数 recursive=False .
print(soup.find_all('p'))
print('-------------')
print(soup.find('p'))
print(soup.find_all('html', recursive=False))

print(soup.p.find_all('p'))


#CSS选择器
#我们在写 CSS 时，标签名不加任何修饰，类名前加点，id名前加 #，
#在这里我们也可以利用类似的方法来筛选元素，用到的方法是 soup.select()，返回类型是 list
#（1）通过标签名查找
print(soup.select('title'))
print(soup.select('a'))

#（2）通过类名查找
print(soup.select('.sister'))

#（3）通过 id 名查找
print(soup.select('#link1'))

#（4）组合查找
#例如查找 p 标签中，id 等于 link1的内容，二者需要用空格分开
print(soup.select('p #link1')) #只能标签和类或者标签和id组合才能查找，不能类和id组合查找


#直接子标签查找
print(soup.select('head > title'))
print(soup.select('p > a'))
print(soup.select('html > head'))

#（5）属性查找
#查找时还可以加入属性元素，属性需要用中括号括起来，注意属性和标签属于同一节点，所以中间不能加空格，否则会无法匹配到。
print(soup.select('a[class="sister"]'))
print(soup.select('a[href="http://example.com/elsie"]'))

#同样，属性仍然可以与上述查找方式组合，不在同一节点的空格隔开，同一节点的不加空格
print(soup.select('p a[id="link2"]'))

#以上的 select 方法返回的结果都是列表形式，可以遍历形式输出，然后用 get_text() 方法来获取它的内容。
soup1 = bs4.BeautifulSoup(html, 'lxml')
print(type(soup1.select('title')))
print(soup1.select('title')[0].get_text())

for title in soup1.select('title'):
	print(title.get_text())



#soup.select('tagname.class1.class2')[0] 
#soup.find('tagname', class_=['class1', 'class2']) 
#都可以获得同时属于多个class的标签