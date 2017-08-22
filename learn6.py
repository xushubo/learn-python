name=('Michael','Bob','Tracy')#另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
#可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。
#不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
t=()#定义一个空的tuple，可以写成()
t=(1)#定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，
#又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
t=(1,)#只有1个元素的tuple定义时必须加一个逗号,来消除歧义
y=('a','b',['A','B'])
print (y)
y[2][0]='X'#tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。
y[2][1]='Y'
print(y,t)
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0],L[1][1],L[2][2])