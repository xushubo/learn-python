#Python内建的filter()函数用于过滤序列。filter()也接收一个函数和一个序列。和map()不同的是，
#filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
#在一个list中，删掉偶数，只保留奇数，可以这么写：
def is_odd(n):
    return n % 2 == 1
L= list(filter(is_odd, [1,3,5,4,7,8,9]))
print(L)
#把一个序列中的空字符串删掉，可以这么写：
def not_empty(s):
    return s and s.strip()
M = list(filter(not_empty, ['a', '   ', '       ', 'bcd']))
print(M)

'''函数原型
声明：s为字符串，rm为要删除的字符序列
s.strip(rm)        删除s字符串中开头、结尾处，位于 rm删除序列的字符
s.lstrip(rm)       删除s字符串中开头处，位于 rm删除序列的字符
s.rstrip(rm)      删除s字符串中结尾处，位于 rm删除序列的字符
注意：
1. 当rm为空时，默认删除空白符（包括'\n', '\r',  '\t',  ' ')
'''

#用filter()这个高阶函数，关键在于正确实现一个“筛选”函数。
#注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，
#需要用list()函数获得所有结果并返回list。

'''用filter求素数:
计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：

首先，列出从2开始的所有自然数，构造一个序列：

2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：

3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：

5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取新序列的第一个数5，然后用5把序列的5的倍数筛掉：

7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

不断筛下去，就可以得到所有的素数。
'''
#用Python来实现这个算法，可以先构造一个从3开始的奇数序列：
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

#然后定义一个筛选函数：
def _not_divisible(n):
    return lambda x: x % n > 0

#最后，定义一个生成器，不断返回下一个素数：
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)
#这个生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列。

#由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：
for n in primes():
    if n < 20:
        print(n, end=' ')
    else:
        break

#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：
def is_palindrome(n):
    s = str(n)
    return s == s[::-1]
'''
def is_palindrome(n):
    I,m=n,0
    while I:
        m=m*10+I%10
        I=I//10
    return(n==m)
'''
'''
实现字符倒转的python函数
方法一，使用[::-1]： 
s = 'python' 
print s[::-1] 

方法二，使用reverse()方法： 
l = list(s) 
l.reverse() 
print ''.join(l) 
'''
N = list(filter(is_palindrome, range(100)))
print(N)

