#!/usr/bin/python3
# coding=utf-8



###### Python3 基础语法
print("\n\n~~~~~~~~~~~~~~~~~~~~~Python3 基础语法~~~~~~~~~~~~~~~~~~~~~")

## python保留字
print("\n\n=====python保留字=====")
import keyword
print (keyword.kwlist)



## 注释
print("\n\n=====注释=====")
# 第一个注释
print ("Hello, Python!") # 第二个注释

# 第一个注释
# 第二个注释

'''
第三注释
第四注释
'''

"""
第五注释
第六注释
"""




## 行与缩进
print("\n\n=====行与缩进=====")
if True:
    print ("True")
else:
    print ("False")

if True:
    print ("Answer")
    print ("True")
else:
    print ("Answer")
 # print ("False")    # 缩进不一致，会导致运行错误




## 字符串(String)
print("\n\n=====字符串(String)=====")
word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""
print(paragraph)

str1='Runoob'

print(str1)                 # 输出字符串
print(str1[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str1[0])              # 输出字符串第一个字符
print(str1[2:5])            # 输出从第三个开始到第五个的字符
print(str1[2:])             # 输出从第三个开始的后的所有字符
print(str1 * 2)             # 输出字符串两次
print(str1 + '你好')        # 连接字符串

print('------------------------------')

print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

str1 = 'Runoob'

print (str1)          # 输出字符串
print (str1[0:-1])    # 输出第一个到倒数第二个的所有字符
print (str1[0])       # 输出字符串第一个字符
print (str1[2:5])     # 输出从第三个开始到第五个的字符
print (str1[2:])      # 输出从第三个开始的后的所有字符
print (str1 * 2)      # 输出字符串两次
print (str1 + "TEST") # 连接字符串

print('Ru\noob')
print(r'Ru\noob') # 可以在字符串前面添加一个 r，表示原始字符串

word = 'Python'
print(word[0], word[5])
print(word[-1], word[-6])
'''
Python 字符串不能被改变。向一个索引位置赋值，比如word[0] = 'm'会导致错误。
1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
2、字符串可以用+运算符连接在一起，用*运算符重复。
3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
4、Python中的字符串不能改变。
'''





## 等待用户输入
print("\n\n=====等待用户输入=====")
# input("\n\n按下 enter 键后退出。")



## 同一行显示多条语句
print("\n\n=====同一行显示多条语句=====")
import sys; x = 'runoob'; sys.stdout.write(x + '\n')




## 多个语句构成代码组
print("\n\n=====多个语句构成代码组=====")
name = "xiao";# input("what is your name?")
if name.endswith('tank'):
    print ('hello tank')
elif name.endswith('xiao'):
    print ('hello xiao')
else:
    print ('hello strange')




## Print 输出
print("\n\n=====Print 输出=====")
x="a"
y="b"
# 换行输出
print( x )
print( y )

print('---------')
# 不换行输出 end 关键字
print( x, end=" " )
print( y, end=" " )
print()
# Fibonacci series: 斐波纳契数列
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b





## import 与 from...import
print("\n\n=====import 与 from...import=====")
import sys
print('Python import mode');
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)

from sys import argv,path  #  导入特定的成员
print('python from import')
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path





###### Python3 基本数据类型
print("\n\n~~~~~~~~~~~~~~~~~~~~~Python3 基本数据类型~~~~~~~~~~~~~~~~~~~~~")


## 变量
print("\n\n=====变量=====")
counter = 100          # 整型变量
miles   = 1000.0       # 浮点型变量
name    = "runoob"     # 字符串

print (counter)
print (miles)
print (name)



## 多个变量赋值
print("\n\n=====多个变量赋值=====")
a = b = c = 1
a, b, c = 1, 2+b+a, "runoob"
# 反斜杠\用于赋值换行
d, e, f = \
    a, a, \
    a
g = \
    b
h = a + \
    b
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)



## type()
print("\n\n=====type()=====")
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))



## isinstance()
print("\n\n=====isinstance()=====")
a = 111
print(isinstance(a, int))

class A:
    pass

class B(A):
    pass

print(isinstance(A(), A))  # returns True
print(type(A()) == A)      # returns True
print(isinstance(B(), A))    # returns True
print(type(B()) == A)        # returns False
# type()不会认为子类是一种父类类型。isinstance()会认为子类是一种父类类型。



## del语句删除一些对象引用
print("\n\n=====del语句删除一些对象引用=====")
var1 = 1
var2 = 10
del var1
print(var2)
# del var1, var2 # NameError: name 'var1' is not defined



## List（列表）
print("\n\n=====List（列表）=====")
list1 = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']

print (list1)            # 输出完整列表
print (list1[0])         # 输出列表第一个元素
print (list1[1:3])       # 从第二个开始输出到第三个元素
print (list1[2:])        # 输出从第三个元素开始的所有元素
print (tinylist * 2)    # 输出两次列表
print (list1 + tinylist) # 连接列表

a = [1, 2, 3, 4, 5, 6]
print(a)
a[0] = 9
print(a)
a[2:5] = [13, 14, 15]
print(a)
a[2:5] = [];print(a)
'''
1、List写在方括号之间，元素用逗号隔开。
2、和字符串一样，list可以被索引和切片。
3、List可以使用+操作符进行拼接。
4、List中的元素是可以改变的。

Python中列表是可变的，这是它区别于字符串和元组的最重要的特点，一句话概括即：列表可以修改，而字符串和元组不能。

列表的方法：

'''




## Tuple（元组）
print("\n\n=====Tuple（元组）=====")
tuple1 = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tinytuple = (123, 'runoob')

print (tuple1)             # 输出完整元组
print (tuple1[0])          # 输出元组的第一个元素
print (tuple1[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple1[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple1 + tinytuple) # 连接元组
# 注意构造包含0或1个元素的元组的特殊语法规则。
tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号
print(tup1)
print(tup2)
'''
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
元组中的元素类型也可以不相同
元组与字符串类似，可以被索引且下标索引从0开始，-1 为从末尾开始的位置。

string、list和tuple都属于sequence（序列）。
1、与字符串一样，元组的元素不能修改。
2、元组也可以被索引和切片，方法一样。
3、元组也可以使用+操作符进行拼接。
'''





## Set（集合）
print("\n\n=====Set（集合）=====")
'''
集合（set）是一个无序不重复元素的序列。
基本功能是进行成员关系测试和删除重复元素。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
'''

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)   # 输出集合，重复的元素被自动去掉
# 集合添加、删除
student.add("Tod")
print(student)
student.remove("Tod")
print(student)

# 成员测试
s="Roses";
if(s in student) :
    print(s+'在集合中')
else :
    print(s+'不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
a.add("abc")
print(a)
a.remove("abc")
print(a)
print(a - b)     # a和b的差集
print(a | b)     # a和b的并集
print(a & b)     # a和b的交集
print(a ^ b)     # a和b中不同时存在的元素





## Dictionary（字典）
print("\n\n=====Dictionary（字典）=====")
'''
字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。
键(key)必须使用不可变类型，且不能重复。
在同一个字典中，键(key)必须是唯一的。
'''

dictc = {}
dictc['one'] = "1 - 菜鸟教程"
dictc['one'] = 123
dictc[2]     = "2 - 菜鸟工具"
dictc[2]     = 234

tinydict = {'name': 'runoob','code':1,'code':2, 'site': 'www.runoob.com'}

print (dictc['one'])       # 输出键为 'one' 的值
print (dictc[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值
print(tinydict.get("site"))

# 构造函数 dict() 可以直接从键值对序列中构建字典
a=dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
print(a)
a.clear()
print(a)
print(dict(Runoob=1, Google=2, Taobao=3))

print({x: x**3 for x in (2, 4, 6)})# x**n表示x的n次方



## Python数据类型转换
print("\n\n=====Python数据类型转换=====")

# int(x [,base]) 将x转换为一个整数,base -- 进制数，默认十进制。
print(int('12',16))        # 如果是带参数base的话，12要以字符串的形式进行输入，12 为 16进制，结果为18
print(int(3.6))

# float(x) 将x转换到一个浮点数
print(float(1))
print(float(-123.6))
print(float('123'))     # 字符串

# complex(real [,imag]) 函数用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。如果第一个参数为字符串，则不需要指定第二个参数。
'''
real -- int, long, float或字符串；
imag -- int, long, float；
'''
print(complex(1, 2))
print(complex(1))    # 数字
print(complex("1"))  # 当做字符串处理
# 注意：这个地方在"+"号两边不能有空格，也就是不能写成"1 + 2j"，应该是"1+2j"，否则会报错
print(complex("1+2j"))

# str(x) 将对象 x 转换为字符串
dict1 = {'runoob': 'runoob.com', 'google': 'google.com'}
print(str(dict1))

# repr(x) 将对象 x 转换为表达式字符串,返回一个对象的 string 格式。
dict1 = {'runoob': 'runoob.com', 'google': 'google.com'}
print(repr(dict1))

# eval(str) 用来计算在字符串中的有效Python表达式,返回表达式的值。
x = 7
print(eval( '3 * x' ))
print(eval('pow(2,2)'))
print(eval('int(\'12\',16)'))

# tuple(s) 将序列 s 转换为一个元组
list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
print(tuple(list1))

# list(s) 将序列 s 转换为一个列表
aTuple = (123, 'Google', 'Runoob', 'Taobao')
print(list(aTuple))
s="Hello World"
print(list(s))

# set(s) 转换为可变集合.函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
x = set('runoob')
y = set('google')
print(x)            # 去重
print(x & y)         # 交集
print(x | y)         # 并集
print(x - y)         # 差集

# dict(d) 创建一个字典。d 必须是一个序列 (key,value)元组。
'''
dict 语法：
class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwarg)
参数说明：
**kwargs -- 关键字
mapping -- 元素的容器。
iterable -- 可迭代对象。
'''
print(dict())                        # 创建空字典
print(dict(a='a', b='b', t='t'))     # 传入关键字
print(dict(zip(['one', 'two', 'three'], [1, 2, 3])))   # 映射函数方式来构造字典
print(dict([('one', 1), ('two', 2), ('three', 3)]))    # 可迭代对象方式来构造字典

# frozenset(s) 转换为不可变集合.返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。s=可迭代的对象，比如列表、字典、元组等等。
a = frozenset(range(10))     # 生成一个新的不可变集合
print(a)
b = frozenset('runoob')
print(b)
# b.add('a')# 'frozenset' object has no attribute 'add'
# print(b)
# b.remove('o')# 'frozenset' object has no attribute 'remove'
# print(b)

# chr(x) 将一个整数转换为一个字符.用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。x可以是10进制也可以是16进制的形式的数字。
print(chr(0x30), chr(0x31), chr(0x61))   # 十六进制
print(chr(48), chr(49), chr(97))         # 十进制

# ord(x) 将一个字符转换为它的整数值.返回对应的 ASCII 数值，或者 Unicode 数值，如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常。x=字符.
print(ord('a'), ord('b'), ord('c'))


# hex(x) 将一个整数转换为一个十六进制字符串.函数用于将10进制整数转换成16进制，以字符串形式表示。
print(hex(255), hex(-42), hex(12))

# oct(x) 将一个整数转换为一个八进制字符串
print(oct(10), oct(20), oct(15))




###### Python3 解释器
print("\n\n~~~~~~~~~~~~~~~~~~~~~Python3 解释器~~~~~~~~~~~~~~~~~~~~~")

'''
Linux/Unix的系统上，一般默认的 python 版本为 2.x，我们可以将 python3.x 安装在 /usr/local/python3 目录中。
安装完成后，我们可以将路径 /usr/local/python3/bin 添加到您的 Linux/Unix 操作系统的环境变量中，这样您就可以通过 shell 终端输入下面的命令来启动 Python3。
如：
$ PATH=$PATH:/usr/local/python3/bin/python3    # 设置环境变量
$ python3 --version
Python 3.4.0
'''

## 脚本式编程
'''
将如下代码拷贝至 hello.py文件中：
print ("Hello, Python!");
通过以下命令执行该脚本：
python3 hello.py
输出结果为：
Hello, Python!
在Linux/Unix系统中，你可以在脚本顶部添加以下命令让Python脚本可以像SHELL脚本一样可直接执行：
#! /usr/bin/env python3
然后修改脚本权限，使其有执行权限，命令如下：
$ chmod +x hello.py
执行以下命令：
./hello.py
输出结果为：
Hello, Python!
'''





###### Python3 运算符
print("\n\n~~~~~~~~~~~~~~~~~~~~~Python3 运算符~~~~~~~~~~~~~~~~~~~~~")

## Python算术运算符
"""
以下假设变量a为10，变量b为21：
/	除 - x 除以 y	b / a 输出结果 2.1
%	取模 - 返回除法的余数	b % a 输出结果 1
**	幂 - 返回x的y次幂	a**b 为10的21次方
//	取整除 - 返回商的整数部分	9//2 输出结果 4 , 9.0//2.0 输出结果 4.0
"""




## Python比较运算符
'''
同java
'''



## Python赋值运算符
'''
以下假设变量a为10，变量b为20：
+=	加法赋值运算符	c += a 等效于 c = c + a
-=	减法赋值运算符	c -= a 等效于 c = c - a
*=	乘法赋值运算符	c *= a 等效于 c = c * a
/=	除法赋值运算符	c /= a 等效于 c = c / a
%=	取模赋值运算符	c %= a 等效于 c = c % a
**=	幂赋值运算符	c **= a 等效于 c = c ** a
//=	取整除赋值运算符	c //= a 等效于 c = c // a
'''




## Python位运算符
'''
按位运算符是把数字看作二进制来进行计算的。
下表中变量 a 为 60，b 为 13二进制格式如下：
a = 0011 1100
b = 0000 1101
-----------------
&	按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0	(a & b) 输出结果 12 ，二进制解释： 0000 1100

|	按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。	(a | b) 输出结果 61 ，二进制解释： 0011 1101

^	按位异或运算符：当两对应的二进位相异时，结果为1	(a ^ b) 输出结果 49 ，二进制解释： 0011 0001

~	按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。~x 类似于 -x-1	(~a ) 输出结果 -61 ，二进制解释： 1100 0011， 在一个有符号二进制数的补码形式。

<<	左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。	a << 2 输出结果 240 ，二进制解释： 1111 0000

>>	右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数	a >> 2 输出结果 15 ，二进制解释： 0000 1111
'''




## Python逻辑运算符
print("\n\n=====Python逻辑运算符=====")
'''
以下假设变量 a 为 10, b为 20:
and	x and y	布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	(a and b) 返回 20。

or	x or y	布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。	(a or b) 返回 10。

not	not x	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not(a and b) 返回 False
'''

a = 10
b = 20
if ( a and b ):
    print ("1 - 变量 a 和 b 都为 true")
else:
    print ("1 - 变量 a 和 b 有一个不为 true")
if ( a or b ):
    print ("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print ("2 - 变量 a 和 b 都不为 true")
# 修改变量 a 的值
a = 0
if ( a and b ):
    print ("3 - 变量 a 和 b 都为 true")
else:
    print ("3 - 变量 a 和 b 有一个不为 true")
if ( a or b ):
    print ("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print ("4 - 变量 a 和 b 都不为 true")
if not( a and b ):
    print ("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
    print ("5 - 变量 a 和 b 都为 true")



## Python成员运算符
print("\n\n=====Python成员运算符=====")
'''
in	如果在指定的序列中找到值返回 True，否则返回 False。	x 在 y 序列中 , 如果 x 在 y 序列中返回 True。

not in	如果在指定的序列中没有找到值返回 True，否则返回 False。	x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。
'''

a = 10
b = 20
list1 = [1, 2, 3, 4, 5 ];
if ( a in list1 ):
    print ("1 - 变量 a 在给定的列表中")
else:
    print ("1 - 变量 a 不在给定的列表中")
if ( b not in list1 ):
    print ("2 - 变量 b 不在给定的列表中")
else:
    print ("2 - 变量 b 在给定的列表中")
# 修改变量 a 的值
a = 2
if ( a in list1 ):
    print ("3 - 变量 a 在给定的列表中")
else:
    print ("3 - 变量 a 不在给定的列表中")




## Python身份运算符
print("\n\n=====Python身份运算符=====")
'''
身份运算符用于比较两个对象的存储单元

is	is 是判断两个标识符是不是引用自一个对象	x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False

is not	is not 是判断两个标识符是不是引用自不同对象	x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。

注： id() 函数用于获取对象内存地址。
'''

a = 20
b = 20
if ( a is b ):
    print ("1 - a 和 b 有相同的标识")
else:
    print ("1 - a 和 b 没有相同的标识")
if ( id(a) == id(b) ):
    print ("2 - a 和 b 有相同的标识")
else:
    print ("2 - a 和 b 没有相同的标识")
# 修改变量 b 的值
b = 30
if ( a is b ):
    print ("3 - a 和 b 有相同的标识")
else:
    print ("3 - a 和 b 没有相同的标识")
if ( a is not b ):
    print ("4 - a 和 b 没有相同的标识")
else:
    print ("4 - a 和 b 有相同的标识")




## Python运算符优先级
'''
列出了从最高到最低优先级的所有运算符：
**	指数 (最高优先级)
~ + -	按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
* / % //	乘，除，取模和取整除
+ -	加法减法
>> <<	右移，左移运算符
&	位 'AND'
^ |	位运算符
<= < > >=	比较运算符
<> == !=	等于运算符
= %= /= //= -= += *= **=	赋值运算符
is is not	身份运算符
in not in	成员运算符
not or and	逻辑运算符
'''



###### Python3 数字(Number)
print("\n\n~~~~~~~~~~~~~~~~~~~~~Python3 数字(Number)~~~~~~~~~~~~~~~~~~~~~")
'''
Python 支持三种不同的数值类型：

整型(Int) - 通常被称为是整型或整数，是正或负整数，不带小数点。Python3 整型是没有限制大小的，可以当作 Long 类型使用，所以 Python3 没有 Python2 的 Long 类型。

浮点型(float) - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）

复数( (complex)) - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。
'''
# 我们可以使用十六进制和八进制来代表整数：
number = 0xA0F # 十六进制
print(number)
number=0o37 # 八进制
print(number)

# Python 数字类型转换
'''
int(x) 将x转换为一个整数。
float(x) 将x转换到一个浮点数。
complex(x) 将x转换到一个复数，实数部分为 x，虚数部分为 0。
complex(x, y) 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。
'''

# Python 数字运算
'''
不同类型的数混合运算时会将整数转换为浮点数
'''
print(3 * 3.75 / 1.5)
print(7.0 / 3)
print(7 / 3)
'''
在交互模式中，最后被输出的表达式结果被赋值给变量 _ 。例如：
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
此处， _ 变量应被用户视为只读变量。
'''

# 数学函数
'''
abs(x)  返回数字的绝对值，如abs(-10) 返回 10

ceil(x) 返回数字的上入整数，如math.ceil(4.1) 返回 5

cmp(x, y)   如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 Python 3 已废弃 。使用 使用 (x>y)-(x<y) 替换。

exp(x)	返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045

fabs(x) 返回数字的绝对值，如math.fabs(-10) 返回10.0

floor(x)	返回数字的下舍整数，如math.floor(4.9)返回 4

log(x)	如math.log(math.e)返回1.0,math.log(100,10)返回2.0

log10(x)	返回以10为基数的x的对数，如math.log10(100)返回 2.0

max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。

min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。

modf(x)	返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。

pow(x, y)	x**y 运算后的值。

round(x [,n])	返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。

sqrt(x)	返回数字x的平方根。
'''

# 随机数函数
'''
随机数可以用于数学，游戏，安全等领域中，还经常被嵌入到算法中，用以提高算法效率，并提高程序的安全性。
Python包含以下常用随机数函数：

choice(seq)	从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。

randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1

random()	随机生成下一个实数，它在[0,1)范围内。

seed([x])	改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。

shuffle(lst)	将序列的所有元素随机排序

uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。
'''

# 三角函数
'''
acos(x)	返回x的反余弦弧度值。
asin(x)	返回x的反正弦弧度值。
atan(x)	返回x的反正切弧度值。
atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值。
cos(x)	返回x的弧度的余弦值。
hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)。
sin(x)	返回的x弧度的正弦值。
tan(x)	返回x弧度的正切值。
degrees(x)	将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
radians(x)	将角度转换为弧度
'''

# 数学常量
'''
pi	数学常量 pi（圆周率，一般以π来表示）
e	数学常量 e，e即自然常数（自然常数）。
'''



###### Python3 字符串
print("\n\n~~~~~~~~~~~~~~~~~~~~~Python3 字符串~~~~~~~~~~~~~~~~~~~~~")

# Python 访问字符串中的值
'''
Python 不支持单字符类型，单字符在 Python 中也是作为一个字符串使用。
Python 访问子字符串，可以使用方括号来截取字符串
'''
var1 = 'Hello World!'
var2 = "Runoob"
print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])

# Python字符串更新
'''
可以截取字符串的一部分并与其他字段拼接
'''
var1 = 'Hello World!'
print ("已更新字符串 : ", var1[:6] + 'Runoob!')

# Python转义字符
'''
在需要在字符中使用特殊字符时，python用反斜杠(\)转义字符。

\(在行尾时)	续行符
\	反斜杠符号
'	单引号
"	双引号
a	响铃
b	退格(Backspace)
e	转义
000	空
n	换行
v	纵向制表符
t	横向制表符
r	回车
f	换页
oyy	八进制数，yy代表的字符，例如：\12代表换行
xyy	十六进制数，yy代表的字符，例如：\x0a代表换行
other	其它的字符以普通格式输出
'''
print('a\x0aa')# 换行
print('a\12a')# 换行

# Python字符串运算符
'''
下表实例变量a值为字符串 "Hello"，b变量值为 "Python"：
+	字符串连接	a + b 输出结果： HelloPython

*	重复输出字符串	a*2 输出结果：HelloHello

[]	通过索引获取字符串中字符	a[1] 输出结果 e

[ : ]	截取字符串中的一部分	a[1:4] 输出结果 ell

in	成员运算符 - 如果字符串中包含给定的字符返回 True	'H' in a 输出结果 1

not in	成员运算符 - 如果字符串中不包含给定的字符返回 True	'M' not in a 输出结果 1

r/R	原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母 r（可以大小写）以外，与普通字符串有着几乎完全相同的语法。	

%	格式字符串	请看下一节内容。
'''
a = "Hello"
b = "Python"
print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])
if( "H" in a) :
    print("H 在变量 a 中")
else :
    print("H 不在变量 a 中")
if( "M" not in a) :
    print("M 不在变量 a 中")
else :
    print("M 在变量 a 中")
print (r'\n')# 输出\n
print (R'\n')# 输出\n

# Python字符串格式化
'''
Python 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，但最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中。
在 Python 中，字符串格式化使用与 C 中 sprintf 函数一样的语法。

python字符串格式化符号:
%c	 格式化字符及其ASCII码
%s	 格式化字符串
%d	 格式化整数
%u	 格式化无符号整型
%o	 格式化无符号八进制数
%x	 格式化无符号十六进制数
%X	 格式化无符号十六进制数（大写）
%f	 格式化浮点数字，可指定小数点后的精度
%e	 用科学计数法格式化浮点数
%E	 作用同%e，用科学计数法格式化浮点数
%g	 %f和%e的简写
%G	 %f 和 %E 的简写
%p	 用十六进制数格式化变量的地址

格式化操作符辅助指令:
*	定义宽度或者小数点精度

-	用做左对齐

+	在正数前面显示加号( + )

<sp>	在正数前面显示空格

#	在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')

0	显示的数字前面填充'0'而不是默认的空格

%	'%%'输出一个单一的'%'

(var)	映射变量(字典参数)

m.n.	m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)
'''
print ("我叫 %s 今年 %d 岁!" % ('小明', 10))

# Python三引号
'''
python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。
'''
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print (para_str)
'''
三引号让程序员从引号和特殊字符串的泥潭里面解脱出来，自始至终保持一小块字符串的格式是所谓的WYSIWYG（所见即所得）格式的。
一个典型的用例是，当你需要一块HTML或者SQL时，这时用字符串组合，特殊字符串转义将会非常的繁琐。
'''
errHTML = '''
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>
'''
print(errHTML % ('三引号'))

# Unicode 字符串
'''
在Python2中，普通字符串是以8位ASCII码进行存储的，而Unicode字符串则存储为16位unicode字符串，这样能够表示更多的字符集。使用的语法是在字符串前面加上前缀 u。
在Python3中，所有的字符串都是Unicode字符串。
'''

# Python 的字符串内建函数
'''
1	
capitalize()
将字符串的第一个字符转换为大写

2	
center(width, fillchar)
返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。

3	
count(str, beg= 0,end=len(string))
返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数

4	
bytes.decode(encoding="utf-8", errors="strict")
Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回。

5	
encode(encoding='UTF-8',errors='strict')
以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'

6	
endswith(suffix, beg=0, end=len(string))
检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.

7	
expandtabs(tabsize=8)
把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。

8	
find(str, beg=0 end=len(string))
检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1

9	
index(str, beg=0, end=len(string))
跟find()方法一样，只不过如果str不在字符串中会报一个异常.

10	
isalnum()
如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False

11	
isalpha()
如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False

12	
isdigit()
如果字符串只包含数字则返回 True 否则返回 False..

13	
islower()
如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False

14	
isnumeric()
如果字符串中只包含数字字符，则返回 True，否则返回 False

15	
isspace()
如果字符串中只包含空白，则返回 True，否则返回 False.

16	
istitle()
如果字符串是标题化的(见 title())则返回 True，否则返回 False

17	
isupper()
如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False

18	
join(seq)
以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串

19	
len(string)
返回字符串长度

20	
ljust(width[, fillchar])
返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。

21	
lower()
转换字符串中所有大写字符为小写.

22	
lstrip()
截掉字符串左边的空格或指定字符。

23	
maketrans()
创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。

24	
max(str)
返回字符串 str 中最大的字母。

25	
min(str)
返回字符串 str 中最小的字母。

26	
replace(old, new [, max])
把 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。

27	
rfind(str, beg=0,end=len(string))
类似于 find()函数，不过是从右边开始查找.

28	
rindex( str, beg=0, end=len(string))
类似于 index()，不过是从右边开始.

29	
rjust(width,[, fillchar])
返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串

30	
rstrip()
删除字符串字符串末尾的空格.

31	
split(str="", num=string.count(str))
num=string.count(str)) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num 个子字符串

32	
splitlines([keepends])
按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。

33	
startswith(str, beg=0,end=len(string))
检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。

34	
strip([chars])
在字符串上执行 lstrip()和 rstrip()

35	
swapcase()
将字符串中大写转换为小写，小写转换为大写

36	
title()
返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())

37	
translate(table, deletechars="")
根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中

38	
upper()
转换字符串中的小写字母为大写

39	
zfill (width)
返回长度为 width 的字符串，原字符串右对齐，前面填充0

40	
isdecimal()
检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。
'''



###### Python3 列表
print("\n\n~~~~~~~~~~~~~~~~~~~~~Python3 列表~~~~~~~~~~~~~~~~~~~~~")

'''
序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。
Python有6个序列的内置类型，但最常见的是列表和元组。
序列都可以进行的操作包括索引，切片，加，乘，检查成员。
此外，Python已经内置确定序列的长度以及确定最大和最小的元素的方法。
列表是最常用的Python数据类型，它可以作为一个方括号[]内的逗号分隔值出现。
列表的数据项不需要具有相同的类型
创建一个列表，只要把逗号分隔的不同的数据项使用方括号[]括起来即可。
'''
# 访问列表中的值
list1 = ['Google', 'Runoob', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])

# 更新列表
'''
可以对列表的数据项进行修改或更新，可以使用append()方法来添加列表项
'''
list1 = ['Google', 'Runoob', 1997, 2000]
print ("第三个元素为 : ", list1[2])
list1[2] = 2001
print ("更新后的第三个元素为 : ", list1[2])
list1.append(2018)
print (list1)

# 删除列表元素
list1 = ['Google', 'Runoob', 1997, 2000]
print (list1)
del list1[2]
print ("删除第三个元素 : ", list1)
list1.remove(2000)
print(list1)

# Python列表脚本操作符
'''
len([1, 2, 3])	3	长度

[1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	组合

['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	重复

3 in [1, 2, 3]	True	元素是否存在于列表中

for x in [1, 2, 3]: print(x, end=" ")	1 2 3	迭代
'''
for x in [1, 2, 3]: print(x, end=" ")
print()

# Python列表截取与拼接
L=['Google', 'Runoob', 'Taobao']
print(L[-2])
print(L[1:])
squares = [1, 4, 9, 16, 25]
print(squares + [36, 49, 64, 81, 100])

# 嵌套列表
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])

# Python列表函数&方法
'''
Python包含以下函数:
1	len(list)
列表元素个数

2	max(list)
返回列表元素最大值

3	min(list)
返回列表元素最小值

4	list(seq)
将元组转换为列表

Python包含以下方法:
1	list.append(obj)
在列表末尾添加新的对象

2	list.count(obj)
统计某个元素在列表中出现的次数

3	list.extend(seq)
在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）

4	list.index(obj)
从列表中找出某个值第一个匹配项的索引位置

5	list.insert(index, obj)
将对象插入列表

6	list.pop(obj=list[-1])
移除列表中的一个元素（默认最后一个元素），并且返回该元素的值

7	list.remove(obj)
移除列表中某个值的第一个匹配项

8	list.reverse()
反向列表中元素

9	list.sort([func])
对原列表进行排序

10	list.clear()
清空列表

11	list.copy()
复制列表
'''



###### Python3 元组
print("\n\n~~~~~~~~~~~~~~~~~~~~~Python3 元组~~~~~~~~~~~~~~~~~~~~~")
'''
Python 的元组与列表类似，不同之处在于元组的元素不能修改。
元组使用小括号()，列表使用方括号[]。
元组创建很简单，只需要在括号中()添加元素，并使用逗号隔开即可。
'''
tup3 = "a", "b", "c", "d";   #  不需要括号也可以
print(type(tup3))
'''
元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用
'''
tup1 = (50)
print(type(tup1))     # 不加逗号，类型为整型
tup1 = (50,)
print(type(tup1))     # 加上逗号，类型为元组

# 访问元组
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])

# 修改元组
'''
元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
'''
tup1 = (12, 34.56);
tup2 = ('abc', 'xyz')
# tup1[0] = 100# 修改元组元素操作是非法的。
# 创建一个新的元组
tup3 = tup1 + tup2;
print (tup3)

# 删除元组
'''
元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
'''
tup1 = ('Google', 'Runoob', 1997, 2000)
print (tup1)
del tup1;
# print ("删除后的元组 tup : ")
# print (tup1)# 元组被删除后，输出变量会有异常信息

# 元组运算符
'''
len((1, 2, 3))	3	计算元素个数

(1, 2, 3) + (4, 5, 6)	(1, 2, 3, 4, 5, 6)	连接

('Hi!',) * 4	('Hi!', 'Hi!', 'Hi!', 'Hi!')	复制

3 in (1, 2, 3)	True	元素是否存在

for x in (1, 2, 3): print (x,)	1 2 3	迭代
'''
for x in (1, 2, 3): print (x,)

# 元组索引，截取
L = ('Google', 'Taobao', 'Runoob')
print(L[2])
print(L[-2])
print(L[1:])

# 元组内置函数
'''
1	len(tuple)
计算元组元素个数。	
>>> tuple1 = ('Google', 'Runoob', 'Taobao')
>>> len(tuple1)
3
>>> 

2	max(tuple)
返回元组中元素最大值。	
>>> tuple2 = ('5', '4', '8')
>>> max(tuple2)
'8'
>>> 

3	min(tuple)
返回元组中元素最小值。	
>>> tuple2 = ('5', '4', '8')
>>> min(tuple2)
'4'
>>> 

4	tuple(seq)
将列表转换为元组。	
>>> list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
>>> tuple1=tuple(list1)
>>> tuple1
('Google', 'Taobao', 'Runoob', 'Baidu')
'''




###### Python3 字典
print("\n\n~~~~~~~~~~~~~~~~~~~~~Python3 字典~~~~~~~~~~~~~~~~~~~~~")
'''
字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中
'''

# 访问字典里的值
dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict1['Name'])
print ("dict['Age']: ", dict1['Age'])

# 修改字典
dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
dict1['Age'] = 8;               # 更新 Age
dict1['School'] = "菜鸟教程"  # 添加信息
print ("dict['Age']: ", dict1['Age'])
print ("dict['School']: ", dict1['School'])
del dict1['Name'] # 删除键 'Name'
print(dict1)
dict1.clear()     # 清空字典
print(dict1)
del dict1         # 删除字典
# print(dict1)#删除字典后字典不再存在，报错

# 字典键的特性
'''
1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
'''
dict1 = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
print ("dict['Name']: ", dict1['Name'])
# dict1 = {['Name']: 'Runoob', 'Age': 7}#报错

# 字典内置函数&方法
'''
Python字典包含了以下内置函数：
1	len(dict)
计算字典元素个数，即键的总数。	
>>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
>>> len(dict)
3

2	str(dict)
输出字典，以可打印的字符串表示。	
>>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
>>> str(dict)
"{'Name': 'Runoob', 'Class': 'First', 'Age': 7}"

3	type(variable)
返回输入的变量类型，如果变量是字典就返回字典类型。	
>>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
>>> type(dict)
<class 'dict'>

Python字典包含了以下内置方法：
1	radiansdict.clear()
删除字典内所有元素

2	radiansdict.copy()
返回一个字典的浅复制

3	radiansdict.fromkeys()
创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值

4	radiansdict.get(key, default=None)
返回指定键的值，如果值不在字典中返回default值

5	key in dict
如果键在字典dict里返回true，否则返回false

6	radiansdict.items()
以列表返回可遍历的(键, 值) 元组数组

7	radiansdict.keys()
以列表返回一个字典所有的键

8	radiansdict.setdefault(key, default=None)
和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default

9	radiansdict.update(dict2)
把字典dict2的键/值对更新到dict里

10	radiansdict.values()
以列表返回字典中的所有值

11	pop(key[,default])
删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。

12	popitem()
随机返回并删除字典中的一对键和值(一般删除末尾对)。
'''




###### Python3 条件控制
print("\n\n~~~~~~~~~~~~~~~~~~~~~Python3 条件控制~~~~~~~~~~~~~~~~~~~~~")
'''
Python 中用 elif 代替了 else if，所以if语句的关键字为：if – elif – else。
注意：
1、每个条件后面要使用冒号（:），表示接下来是满足条件后要执行的语句块。
2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
3、在Python中没有switch – case语句。
4、等于0为false
'''
var2 = -0.1
if var2:
    print ("if 表达式条件为 true")
    print (var2)
else:
    print ("if 表达式条件为 false")
    print (var2)

# if 嵌套
'''
在嵌套 if 语句中，可以把 if...elif...else 结构放在另外一个 if...elif...else 结构中。
if 表达式1:
    语句
    if 表达式2:
        语句
    elif 表达式3:
        语句
    else:
        语句
elif 表达式4:
    语句
else:
    语句
'''




###### Python3 循环语句
print("\n\n~~~~~~~~~~~~~~~~~~~~~Python3 循环语句~~~~~~~~~~~~~~~~~~~~~")
'''
Python中的循环语句有 for 和 while。
Python中没有do..while循环。

while语句的一般形式：
while 判断条件：
    语句
    
for循环的一般格式如下：
for <variable> in <sequence>:
    <statements>
else:
    <statements>
    
无限循环你可以使用 CTRL+C 来中断循环。
'''

# 使用 else 语句
count = 0
while count < 5:
    print (count, " 小于 5")
    count = count + 1
else:
    print (count, " 大于或等于 5")
sites = []
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

# range()函数
for i in range(5):
    print(i)
print()
for i in range(5,9) :# 在5到9之间(>=5，<9)以1为步长循环
    print(i)
print()
for i in range(0, 10, 3) :# 在0到10之间以3为步长循环
    print(i)
print()
for i in range(-10, -100, -30) :# 在-10到-100(>=-10，<-100)之间以-30为步长循环
    print(i)
print()
'''
range()和len()函数以遍历一个序列的索引
可以使用range()函数来创建一个列表
'''
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])
print()
print(list(range(5)))

# break和continue语句
'''
同java
'''

# pass 语句
'''
Python pass是空语句，是为了保持程序结构的完整性。
pass 不做任何事情，一般用做占位语句

eg:
while True:
    pass  # 等待键盘中断 (Ctrl+C)
'''
class MyEmptyClass:
    pass

for letter in 'Runoob':
    if letter == 'o':
        pass
        # print ('执行pass')
    print ('当前字母 :', letter)
print ("Good bye!")




###### Python3 迭代器与生成器
print("\n\n~~~~~~~~~~~~~~~~~~~~~Python3 迭代器与生成器~~~~~~~~~~~~~~~~~~~~~")

# 迭代器
'''
迭代是Python最强大的功能之一，是访问集合元素的一种方式。
迭代器是一个可以记住遍历的位置的对象。
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
迭代器有两个基本的方法：iter() 和 next()。
字符串，列表或元组对象都可用于创建迭代器。
'''
list1=[1,2,3,4]
it = iter(list1)    # 创建迭代器对象
print (next(it))   # 输出迭代器的下一个元素
print (next(it))   # 输出迭代器的下一个元素
'''
迭代器对象可以使用常规for语句进行遍历
'''
list1=[1,2,3,4]
it = iter(list1)    # 创建迭代器对象
for x in it:
    print (x, end=" ")
    pass
print()

# 生成器
'''
在 Python 中，使用了 yield 的函数被称为生成器（generator）。
跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
调用一个生成器函数，返回的是一个迭代器对象。
'''
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
print(next(f))
print(next(f))
for x in f:#2个next之后从第3个开始
    print (x, end=" ")
    pass
print()



###### Python3 函数
print("\n\n~~~~~~~~~~~~~~~~~~~~~Python3 函数~~~~~~~~~~~~~~~~~~~~~")

# 定义一个函数
'''
你可以定义一个由自己想要功能的函数，以下是简单的规则：
函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。

一般格式如下：
def 函数名（参数列表）:
    函数体
'''
# 计算面积函数
def area(width, height):
    return width * height
def print_welcome(name):
    print("Welcome", name)
print_welcome("Runoob")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))

def printinfo( name="hello", age=35 ):
    "打印任何传入的字符串"
    print ("名字: ", name)
    print ("年龄: ", age)
    print ("------------------------")
    return
printinfo( age=50, name="runoob" )# 函数参数的使用不需要使用指定顺序
printinfo( 50, "runoob" )
printinfo( "runoob" )# 没有传入 age 参数，则使用默认值
printinfo()

# 不定长参数
'''
你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述2种参数不同，声明时不会命名。
基本语法如下：
def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
加了星号（*）的变量名会存放所有未命名的变量参数。如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。
'''
def printinfo( arg1, *vartuple ):
    "打印任何传入的参数"
    print ("输出: ")
    print (arg1)
    for var in vartuple:
        print (var)
    print("-------------")
    return
printinfo( 10 )
printinfo( 70, 60, 50 )

# 匿名函数
'''
python 使用 lambda 来创建匿名函数。
所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
lambda 只是一个表达式，函数体比 def 简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
虽然lambda函数看起来只能写一行，目的是调用小函数时不占用栈内存从而增加运行效率。

lambda 函数的语法只包含一个语句，如下：
lambda [arg1 [,arg2,.....argn]]:expression
'''
sum = lambda arg1, arg2: arg1 + arg2;
print ("相加后的值为 : ", sum( 10, 20 ))
print ("相加后的值为 : ", sum( 20, 20 ))

# return语句
'''
return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None
'''

# 变量作用域
'''
Python的作用域一共有4种，分别是：
L （Local） 局部作用域
E （Enclosing） 闭包函数外的函数中
G （Global） 全局作用域
B （Built-in） 内建作用域
以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找。
'''
x = int(2.9)  # 内建作用域
g_count = 0  # 全局作用域
def outer():
    o_count = 1*g_count*x  # 闭包函数外的函数中
    def inner():
        i_count = 2*o_count  # 局部作用域
'''
Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问
'''
if True:
    msg = 'I am from Runoob'
print(msg)

# 全局变量和局部变量
total = 0; # 这是一个全局变量
# 可写函数说明
def sum( arg1, arg2 ):
    #返回2个参数的和."
    total = arg1 + arg2; # total在这里是局部变量.
    print ("函数内是局部变量 : ", total)
    return total;
sum( 10, 20 );
print ("函数外是全局变量 : ", total)

# global 和 nonlocal关键字
'''
当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。
'''
num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)
fun1()
'''
如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了
'''
print("------------")
def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)
outer()




###### Python3 数据结构
print("\n\n~~~~~~~~~~~~~~~~~~~~~Python3 数据结构~~~~~~~~~~~~~~~~~~~~~")

## 列表
print("\n\n=====列表=====")
'''
Python中列表是可变的，这是它区别于字符串和元组的最重要的特点，一句话概括即：列表可以修改，而字符串和元组不能。

Python 中列表的方法：
list.append(x)	把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。

list.extend(L)	通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。

list.insert(i, x)	在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。

list.remove(x)	删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。

list.pop([i])	从列表的指定位置删除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被删除。（方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，你会经常在 Python 库参考手册中遇到这样的标记。）

list.clear()	移除列表中的所有项，等于del a[:]。

list.index(x)	返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。

list.count(x)	返回 x 在列表中出现的次数。

list.sort()	对列表中的元素进行排序。

list.reverse()	倒排列表中的元素。

list.copy()	返回列表的浅复制，等于a[:]。
'''
a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x'))
a.insert(2, -1)
a.append(333)
print(a)
print(a.index(333))
# print(a.index('x'))# 如果没有匹配的元素就会返回一个错误。
a.remove(333)
print(a)
a.reverse()
print(a)
a.sort()
print(a)

# 将列表当做堆栈使用
'''
列表方法使得列表可以很方便的作为一个堆栈来使用，堆栈作为特定的数据结构，最先进入的元素最后一个被释放（后进先出）。用 append() 方法可以把一个元素添加到堆栈顶。用不指定索引的 pop() 方法可以把一个元素从堆栈顶释放出来。
'''
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)

# 将列表当作队列使用
'''
也可以把列表当做队列用，只是在队列里第一加入的元素，第一个取出来；但是拿列表用作这样的目的效率不高。在列表的最后添加或者弹出元素速度快，然而在列表里插入或者从头部弹出速度却不快（因为所有其他的元素都得一个一个地移动）。
'''
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue)
print(queue.popleft())
print(queue)
print(queue.popleft())
print(queue)

# 列表推导式
'''
列表推导式提供了从序列创建列表的简单途径。通常应用程序将一些操作应用于某个序列的每个元素，用其获得的结果作为生成新列表的元素，或者根据确定的判定条件创建子序列。
每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。返回结果是一个根据表达从其后的 for 和 if 上下文环境中生成出来的列表。如果希望表达式推导出一个元组，就必须使用括号。
'''
vec = [2, 4, 6]
print([3*x for x in vec])# 这里我们将列表中每个数值乘三，获得一个新的列表
print(vec)
print([[x, x**2] for x in vec])
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print(freshfruit)
print([weapon.strip() for weapon in freshfruit])# 对序列里每一个元素逐个调用某方法：strip()
# 可以用 if 子句作为过滤器
print([3*x for x in vec if x > 3])
print([3*x for x in vec if x < 2])
# 循环和其它技巧
vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print([x*y for x in vec1 for y in vec2])# vec1第n个分别*vec2每个
print([x+y for x in vec1 for y in vec2])
print([x+y for x in vec2 for y in vec1])
print([vec1[i]*vec2[i] for i in range(len(vec1))])
print([str(round(355/113, i)) for i in range(1, 6)])# 列表推导式可以使用复杂表达式或嵌套函数

# 嵌套列表解析
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]# 3X4的矩阵列表
print(matrix)
# 将3X4的矩阵列表转换为4X3列表
# 方法1
print([[row[i] for row in matrix] for i in range(4)])
# 方法2
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)
# 方法3
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)

# del 语句
'''
使用 del 语句可以从一个列表中依索引而不是值来删除一个元素。这与使用 pop() 返回一个值不同。可以用 del 语句从列表中删除一个切割，或清空整个列表（我们以前介绍的方法是给该切割赋一个空列表）
'''
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)
del a# 也可以用 del 删除实体变量
# print(a)# del a后再使用a，报错：name 'a' is not defined

## 元组和序列
print("\n\n=====元组和序列=====")
'''
元组在输出时总是有括号的，以便于正确表达嵌套结构。在输入时可能有或没有括号()，不过括号通常是必须的（如果元组是更大的表达式的一部分）。
'''
t = 12345, 54321, 'hello!'
print(t[0])
print(t)
u = t, (1, 2, 3, 4, 5)# Tuples nested
print(u)

## 集合
print("\n\n=====集合=====")
'''
集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。
可以用大括号{}创建集合。注意：如果要创建一个空集合，你必须用 set() 而不是 {} ；后者创建一个空的字典
'''
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # 删除重复的
print('orange' in basket)                 # 检测成员
print('crabgrass' in basket)
# 以下演示了两个集合的操作
a = set('abracadabra')
b = set('alacazam')
print(a)                                  # a 中唯一的字母
print(a - b)                              # 在 a 中的字母，但不在 b 中
print(a | b)                              # 在 a 或 b 中的字母
print(a & b)                              # 在 a 和 b 中都有的字母
print(a ^ b)                              # 在 a 或 b 中的字母，但不同时在 a 和 b 中
# 集合也支持推导式
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

## 字典
print("\n\n=====字典=====")
'''
序列是以连续的整数为索引，与此不同的是，字典以关键字为索引，关键字可以是任意不可变类型，通常用字符串或数值。
理解字典的最佳方式是把它看做无序的键=>值对集合。在同一个字典之内，关键字必须是互不相同。
一对大括号创建一个空的字典：{}。
'''
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4227# 增加guido
print(tel)
print(tel['jack'])
del tel['sape']# 删除sape
tel['irv'] = 4127
print(tel)
print(list(tel.keys()))
print(list(tel.values()))
print(sorted(tel.keys()))
print(sorted(tel.values()))
print('guido' in tel)
print('jack' not in tel)
# 构造函数 dict() 直接从键值对元组列表中构建字典
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
print(dict(sape=4139, guido=4127, jack=4098))
# 字典推导可以用来创建任意键和值的表达式
print({x: x**2 for x in (2, 4, 6)})

## 遍历技巧
print("\n\n=====遍历技巧=====")
# 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, ":", v)
# 在序列list/tuple/set/str中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到
a=['tic', 'tac', 'toe']
print(type(a))
for i, v in enumerate(a):
    print(i, v)
a=('tic', 'tac', 'toe')
print(type(a))
for i, v in enumerate(a):
    print(i, v)
a={'tic', 'tac', 'toe'}
print(type(a))
for i, v in enumerate(a):
    print(i, v)
a='abcd'
print(type(a))
for i, v in enumerate(a):
    print(i, v)
# 同时遍历两个或更多的序列，可以使用 zip() 组合
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
# 要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数
for i in reversed(range(1, 10, 2)):# 在1到10(>=1，<-10)之间以2为步长循环
    print(i, end=',')
print()
# 要按顺序遍历一个序列，使用 sorted() 函数
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f, end=',')
print()
for f in sorted(basket):
    print(f, end=',')
print()




###### Python3 模块
print("\n\n~~~~~~~~~~~~~~~~~~~~~Python3 模块~~~~~~~~~~~~~~~~~~~~~")
'''
在前面的几个章节中我们脚本上是用 python 解释器来编程，如果你从 Python 解释器退出再进入，那么你定义的所有的方法和变量就都消失了。
为此 Python 提供了一个办法，把这些定义存放在文件中，为一些脚本或者交互式的解释器实例使用，这个文件被称为模块。
模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能。这也是使用 python 标准库的方法。
'''

## import 语句
print("\n\n=====import 语句=====")
'''
想使用 Python 源文件，只需在另一个源文件里执行 import 语句，语法如下：
import module1[, module2[,... moduleN]
当解释器遇到 import 语句，如果模块在当前的搜索路径就会被导入。
搜索路径是一个解释器会先进行搜索的所有目录的列表。如想要导入模块 support，
如Module1.py，Module1Test.py，运行：
E:\workspace_201612\mypy_idea\test\python3>python Module1Test.py
Hello :  Runoob
'''
'''
一个模块只会被导入一次，不管你执行了多少次import。这样可以防止导入模块被一遍又一遍地执行。
当我们使用import语句的时候，Python解释器是怎样找到对应的文件的呢？
这就涉及到Python的搜索路径，搜索路径是由一系列目录名组成的，Python解释器就依次从这些目录中去寻找所引入的模块。
这看起来很像环境变量，事实上，也可以通过定义环境变量的方式来确定搜索路径。
搜索路径是在Python编译或安装的时候确定的，安装新的库应该也会修改。搜索路径被存储在sys模块中的path变量，做一个简单的实验，在交互式解释器中，输入以下代码：
'''
import sys
print(sys.path)
'''
sys.path 输出是一个列表，对于脚本运行的话包含运行的脚本所在的目录，即可以import同目录py文件
'''
import Module1
Module1.print_func("Runoob")
import fibo
fibo.fib(1000)
print(fibo.fib2(100))
print(fibo.__name__)
print(fibo.a)
print(fibo._a)
fib2=fibo.fib# 可以把它赋给一个本地的名称
fib2(1000)

## from…import 语句
print("\n\n=====from…import 语句=====")
'''
Python的from语句让你从模块中导入一个指定的部分到当前命名空间中，语法如下：
from modname import name1[, name2[, ... nameN]]
'''
from fibo import fib
fib(1000)
from fibo import fib2
print(fib2(100))
from fibo import a
print(a)
from fibo import _a
print(_a)

## from…import* 语句
print("\n\n=====from…import* 语句=====")
'''
把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：
from modname import *
'''
from fibo import *
fib(1000)
print(fib2(100))
print(a)

## 深入模块
print("\n\n=====深入模块=====")
'''
模块除了方法定义，还可以包括可执行的代码。这些代码一般用来初始化这个模块。这些代码只有在第一次被导入时才会被执行。
每个模块有各自独立的符号表，在模块内部为所有的函数当作全局符号表来使用。
所以，模块的作者可以放心大胆的在模块内部使用这些全局变量，而不用担心把其他用户的全局变量搞花。
这将把所有的名字都导入进来，但是那些由单一下划线（_）开头的名字不在此例
'''
from fibo import *
fib(1000)
print(fib2(100))
print(a)
# print(_a)# 报错name '_a' is not defined

## __name__属性
print("\n\n=====__name__属性=====")
'''
一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
E:\workspace_201612\mypy_idea\test\python3>python using_name.py
程序自身在运行
'''
import using_name
'''
说明： 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。
说明：__name__ 与 __main__ 底下是双下划线
'''

## dir() 函数
print("\n\n=====dir() 函数=====")
'''
内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回
如果没有给定参数，那么 dir() 函数会罗列出当前定义的所有名称
'''
import sys, fibo, using_name
print(dir(sys))
print(dir(fibo))
print(dir(using_name))
print(dir())
aaaaaaaaaaaaaaaaa = 5 # 建立一个新的变量
print(dir())

## 标准模块
print("\n\n=====标准模块=====")
'''
Python 本身带着一些标准的模块库，在 Python 库参考文档中将会介绍到（就是后面的"库参考文档"）。
有些模块直接被构建在解析器里，这些虽然不是一些语言内置的功能，但是他却能很高效的使用，甚至是系统级调用也没问题。
这些组件会根据不同的操作系统进行不同形式的配置，比如 winreg 这个模块就只会提供给 Windows 系统。
应该注意到这有一个特别的模块 sys ，它内置在每一个 Python 解析器中。变量 sys.ps1 和 sys.ps2 定义了主提示符和副提示符所对应的字符串:
>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C>
'''

## 包
print("\n\n=====包=====")
'''
包是一种管理 Python 模块命名空间的形式，采用"点模块名称"。
比如一个模块的名称是 A.B， 那么他表示一个包 A中的子模块 B 。
就好像使用模块的时候，你不用担心不同模块之间的全局变量相互影响一样，采用点模块名称这种形式也不用担心不同库之间的模块重名的情况。
目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包，主要是为了避免一些滥俗的名字（比如叫做 string）不小心的影响搜索路径中的有效模块。
最简单的情况，放一个空的 :file:__init__.py就可以了。
'''
# 这样导入子模块，必须使用全名去访问
# import test.python3.module.Module2
# test.python3.module.Module2.print_func('aa')
'''
但是：
E:\workspace_201612\mypy_idea\test\python3>python HelloWorld.py报错
'''
# from test.python3.module import Module2
# Module2.print_func('aa')
'''
但是：
E:\workspace_201612\mypy_idea\test\python3>python HelloWorld.py报错
'''
# from test.python3.module.Module2 import print_func
# print_func('aa')
'''
但是：
E:\workspace_201612\mypy_idea\test\python3>python HelloWorld.py报错
'''
'''
注意当使用from package import item这种形式的时候，对应的item既可以是包里面的子模块（子包），或者包里面定义的其他名称，比如函数，类或者变量。
import语法会首先把item当作一个包定义的名称，如果没找到，再试图按照一个模块去导入。如果还没找到，恭喜，一个:exc:ImportError 异常被抛出了。
反之，如果使用形如import item.subitem.subsubitem这种导入形式，除了最后一项，都必须是包，而最后一项则可以是模块或者是包，但是不可以是类，函数或者变量的名字。
'''
# 从一个包中导入*
'''
设想一下，如果我们使用 from sound.effects import *会发生什么？
Python 会进入文件系统，找到这个包里面所有的子模块，一个一个的把它们都导入进来。
但是很不幸，这个方法在 Windows平台上工作的就不是非常好，因为Windows是一个大小写不区分的系统。
在这类平台上，没有人敢担保一个叫做 ECHO.py 的文件导入为模块 echo 还是 Echo 甚至 ECHO。
（例如，Windows 95就很讨厌的把每一个文件的首字母大写显示）而且 DOS 的 8+3 命名规则对长模块名称的处理会把问题搞得更纠结。
为了解决这个问题，只能烦劳包作者提供一个精确的包的索引了。
导入语句遵循如下规则：如果包定义文件 __init__.py 存在一个叫做 __all__ 的列表变量，那么在使用 from package import * 的时候就把这个列表中的所有名字作为包内容导入。
作为包的作者，可别忘了在更新包之后保证 __all__ 也更新.
比如__init__.py中包含如下代码:
__all__ = ["echo", "surround", "reverse"]
这表示当你使用from sound.effects import *这种用法时，你只会导入包里面这三个子模块。
'''




###### Python3 输入和输出
print("\n\n~~~~~~~~~~~~~~~~~~~~~Python3 输入和输出~~~~~~~~~~~~~~~~~~~~~")

## 输出格式美化
print("\n\n=====输出格式美化=====")
'''
Python两种输出值的方式: 表达式语句和 print() 函数。
第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用。
如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
str()： 函数返回一个用户易读的表达形式。
repr()： 产生一个解释器易读的表达形式。
'''
s = 'Hello, Runoob'
print(str(s))
print(repr(s))
print(str(1/7))
x = 10 * 3.25
y = 200 * 200
s = 'x 的值为： ' + repr(x) + ',  y 的值为：' + repr(y) + '...'
print(s)
#  repr() 函数可以转义字符串中的特殊字符
hello = 'hello, runoob\n'
hellos = repr(hello)
print(hellos)
# repr() 的参数可以是 Python 的任何对象
print(repr((x, y, ('Google', 'Runoob'))))
# 输出一个平方与立方的表:
for x in range(1, 11):
	print(repr(x).ljust(2), repr(x*x).center(3), end=' ')
	# 注意前一行 'end' 的使用
	print(repr(x*x*x).rjust(4))
'''
例子中, 每列间的空格由 print() 添加。
这个例子展示了字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。
还有类似的方法, 如 ljust() 和 center()。 这些方法并不会写任何东西, 它们仅仅返回新的字符串。
另一个方法 zfill(), 它会在数字的左边填充 0
'''
print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))
print('3.14159265359'.zfill(50))
# 输出一个平方与立方的表:
for x in range(1, 11):
	print('{1:2d} {0:3d} {2:4d}'.format(x, x*x, x*x*x))
'''
str.format() 的基本使用如下:
1 括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换。
2 在括号中的数字用于指向传入对象在 format() 中的位置.
3 如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数。
4 位置及关键字参数可以任意的结合.
5 '!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化.
6 可选项 ':' 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。
7 在 ':' 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
8 如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情。最简单的就是传入一个字典, 然后使用方括号 '[]' 来访问键值 .
9 使用 '**' 
'''
print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
print('{0} 和 {1}'.format('Google', 'Runoob'))
print('{1} 和 {0}'.format('Google', 'Runoob'))
print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))
print('站点列表 {1}, {0}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))
import math
print('常量 PI 的值近似为： {}。'.format(math.pi))
print('常量 PI 的值近似为： {!r}。'.format(math.pi))
print('常量 PI 的值近似为： {!a}。'.format(math.pi))
print('常量 PI 的值近似为： {!s}。'.format(math.pi))
print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
	print('{0:10} ==> {1:10d}'.format(name, number))
print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))
print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))

## 旧式字符串格式化
print("\n\n=====旧式字符串格式化=====")
'''
% 操作符也可以实现字符串格式化。 它将左边的参数作为格式化字符串, 而将右边的代入.
'''
print('常量 PI 的值近似为：%.5f。' % math.pi)
print('常量 PI 的值近似为：%5.5f。' % math.pi)

## 读取键盘输入
print("\n\n=====读取键盘输入=====")
'''
Python提供了 input() 置函数从标准输入读入一行文本，默认的标准输入是键盘。
input 可以接收一个Python表达式作为输入，并将运算结果返回.
'''
# str1 = input("请输入：")
# print ("你输入的内容是: ", str1)

## 读和写文件
print("\n\n=====读和写文件=====")
'''
open() 将会返回一个 file 对象，基本语法格式如下:
open(filename, mode)
	filename：filename 变量是一个包含了你要访问的文件名称的字符串值。
	mode：mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
不同模式打开文件的完全列表：
r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。

rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。

r+	打开一个文件用于读写。文件指针将会放在文件的开头。

rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。

w	打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。

wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。

w+	打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。

wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。

a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。

ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。

a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。

ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。

模式				r	r+	w	w+	a	a+
读					+	+		+		+
写						+	+	+	+	+
创建						+	+	+	+
覆盖						+	+		
指针在开始			+	+	+	+		
指针在结尾							+	+
'''
filePath="io/foo.txt";
f = open(filePath, "w")# 打开一个文件
f.write( "Python 是一个非常\n好的语言。\n是的，的确非常好!!\n" )
f.close()# 关闭打开的文件
'''
第二个参数描述文件如何使用的字符。 mode 可以是 'r' 如果文件只读, 'w' 只用于写 (如果存在同名文件则将被删除), 和 'a' 用于追加文件内容; 所写的任何数据都会被自动增加到末尾. 'r+' 同时用于读写。 mode 参数是可选的; 'r' 将是默认值。
'''
# 文件对象的方法
'''
f.read()
为了读取一个文件的内容，调用 f.read(size), 这将读取一定数目的数据, 然后作为字符串或字节对象返回。
size 是一个可选的数字类型的参数。 当 size 被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回。

f.readline()
f.readline() 会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。

f.readlines()
f.readlines() 将返回该文件中包含的所有行。
如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割。

注意，实践证明，read readline readlines要重新open才有用.

f.write()
f.write(string) 将 string 写入到文件中, 然后返回写入的字符数。

f.tell()
f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。

f.seek()
如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。
from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如：
seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
seek(x,1) ： 表示从当前位置往后移动x个字符
seek(-x,2)：表示从文件的结尾往前移动x个字符
from_what 值为默认为0，即文件开头。在文本文件中 (那些打开文件的模式下没有 b 的), 只会相对于文件起始位置进行定位。

f.close()
当你处理完一个文件后, 调用 f.close() 来关闭文件并释放系统的资源，如果尝试再调用该文件，则会抛出异常。
当处理一个文件对象时, 使用 with 关键字是非常好的方式。在结束后, 它会帮你正确的关闭文件。 而且写起来也比 try - finally 语句块要简短.
'''
f = open(filePath, "r")
str1 = f.read()
print(str1)
f.close
f = open(filePath, "r")
str1 = f.readline()
print(str1)
f.close()
f = open(filePath, "r")
str1 = f.readlines()# 返回该文件中包含的所有行
print(str1)
f.close()
# 返回该文件中包含的所有行也可以迭代一个文件对象然后读取每行
f = open(filePath, "r")
for line in f:
    print(line, end='')
f.close()
f = open(filePath, "w")
num = f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
print(num)
f.close()
# 如果要写入一些不是字符串的东西, 那么将需要先进行转换
f = open(filePath, "w")
value = ('www.runoob.com', 14)
print("type(value):")
print(type(value))
s = str(value)
f.write(s)
f.close()
filePath2="io/foo2.txt";
f = open(filePath2, 'rb+')
f.write(b'0123456789abcdef')
print(f.seek(5))     # 移动到文件的第六个字节
print(f.read(1))
print(f.seek(-3, 2)) # 移动到文件的倒数第三字节
print(f.read(1))
f.close()
with open(filePath, 'r') as f:
	read_data = f.read()
	print(read_data)
print(f.closed)

## pickle 模块
print("\n\n=====pickle 模块=====")
'''
python的pickle模块实现了基本的数据序列和反序列化。
通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
pickle.dump(obj, file, [,protocol])
'''
import pickle
# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}
filePath3="io/data.pkl";
f = open(filePath3, 'wb')
# Pickle dictionary using protocol 0.
pickle.dump(data1, f)
# Pickle the list using the highest protocol available.
selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)
print(selfref_list)
pickle.dump(selfref_list, f, -1)
f.close()
'''
通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
x = pickle.load(file)
从 file 中读取一个字符串，并将它重构为原来的python对象。
file: 类文件对象，有read()和readline()接口。
'''
import pprint, pickle
#使用pickle模块从文件中重构python对象
f = open(filePath3, 'rb')
data1 = pickle.load(f)#第一次pickle.dump的内容
print(type(data1))
pprint.pprint(data1)
data2 = pickle.load(f)#第二次pickle.dump的内容
print(type(data2))
print(data2)
pprint.pprint(data2)
f.close()




###### Python3 File(文件) 方法
print("\n\n~~~~~~~~~~~~~~~~~~~~~Python3 File(文件) 方法~~~~~~~~~~~~~~~~~~~~~")
'''
file 对象使用 open 函数来创建，下表列出了 file 对象常用的函数：
1
file.close()
关闭文件。关闭后文件不能再进行读写操作。

2
file.flush()
刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。

3
file.fileno()
返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。

4
file.isatty()
如果文件连接到一个终端设备返回 True，否则返回 False。

5
file.next()
返回文件下一行。

6
file.read([size])
从文件读取指定的字节数，如果未给定或为负则读取所有。

7
file.readline([size])
读取整行，包括 "\n" 字符。

8
file.readlines([sizeint])
读取所有行并返回列表，若给定sizeint>0，返回总和大约为sizeint字节的行, 实际读取值可能比 sizeint 较大, 因为需要填充缓冲区。

9
file.seek(offset[, whence])
设置文件当前位置

10
file.tell()
返回文件当前位置。

11
file.truncate([size])
从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；截断之后 V 后面的所有字符被删除，其中 Widnows 系统下的换行代表2个字符大小。

12
file.write(str)
将字符串写入文件，没有返回值。

13
file.writelines(sequence)
向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。
'''




###### Python3 OS 文件/目录方法
print("\n\n~~~~~~~~~~~~~~~~~~~~~Python3 OS 文件/目录方法~~~~~~~~~~~~~~~~~~~~~")
'''
os 模块提供了非常丰富的方法用来处理文件和目录。常用的方法如下表所示：
1
os.access(path, mode)
检验权限模式

2
os.chdir(path)
改变当前工作目录

3
os.chflags(path, flags)
设置路径的标记为数字标记。

4
os.chmod(path, mode)
更改权限

5
os.chown(path, uid, gid)
更改文件所有者

6
os.chroot(path)
改变当前进程的根目录

7
os.close(fd)
关闭文件描述符

8
os.closerange(fd_low, fd_high)
关闭所有文件描述符，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略

9
os.dup(fd)
复制文件描述符 fd

10
os.dup2(fd, fd2)
将一个文件描述符 fd 复制到另一个 fd2

11
os.fchdir(fd)
通过文件描述符改变当前工作目录

12
os.fchmod(fd, mode)
改变一个文件的访问权限，该文件由参数fd指定，参数mode是Unix下的文件访问权限。

13
os.fchown(fd, uid, gid)
修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。

14
os.fdatasync(fd)
强制将文件写入磁盘，该文件由文件描述符fd指定，但是不强制更新文件的状态信息。

15
os.fdopen(fd[, mode[, bufsize]])
通过文件描述符 fd 创建一个文件对象，并返回这个文件对象

16
os.fpathconf(fd, name)
返回一个打开的文件的系统配置信息。name为检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。

17
os.fstat(fd)
返回文件描述符fd的状态，像stat()。

18
os.fstatvfs(fd)
返回包含文件描述符fd的文件的文件系统的信息，像 statvfs()

19
os.fsync(fd)
强制将文件描述符为fd的文件写入硬盘。

20
os.ftruncate(fd, length)
裁剪文件描述符fd对应的文件, 所以它最大不能超过文件大小。

21
os.getcwd()
返回当前工作目录

22
os.getcwdu()
返回一个当前工作目录的Unicode对象

23
os.isatty(fd)
如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。

24
os.lchflags(path, flags)
设置路径的标记为数字标记，类似 chflags()，但是没有软链接

25
os.lchmod(path, mode)
修改连接文件权限

26
os.lchown(path, uid, gid)
更改文件所有者，类似 chown，但是不追踪链接。

27
os.link(src, dst)
创建硬链接，名为参数 dst，指向参数 src

28
os.listdir(path)
返回path指定的文件夹包含的文件或文件夹的名字的列表。

29
os.lseek(fd, pos, how)
设置文件描述符 fd当前位置为pos, how方式修改: SEEK_SET 或者 0 设置从文件开始的计算的pos; SEEK_CUR或者 1 则从当前位置计算; os.SEEK_END或者2则从文件尾部开始. 在unix，Windows中有效

30
os.lstat(path)
像stat(),但是没有软链接

31
os.major(device)
从原始的设备号中提取设备major号码 (使用stat中的st_dev或者st_rdev field)。

32
os.makedev(major, minor)
以major和minor设备号组成一个原始设备号

33
os.makedirs(path[, mode])
递归文件夹创建函数。像mkdir(), 但创建的所有intermediate-level文件夹需要包含子文件夹。

34
os.minor(device)
从原始的设备号中提取设备minor号码 (使用stat中的st_dev或者st_rdev field )。

35
os.mkdir(path[, mode])
以数字mode的mode创建一个名为path的文件夹.默认的 mode 是 0777 (八进制)。

36
os.mkfifo(path[, mode])
创建命名管道，mode 为数字，默认为 0666 (八进制)

37
os.mknod(filename[, mode=0600, device])
创建一个名为filename文件系统节点（文件，设备特别文件或者命名pipe）。

38
os.open(file, flags[, mode])
打开一个文件，并且设置需要的打开选项，mode参数是可选的

39
os.openpty()
打开一个新的伪终端对。返回 pty 和 tty的文件描述符。

40
os.pathconf(path, name)
返回相关文件的系统配置信息。

41
os.pipe()
创建一个管道. 返回一对文件描述符(r, w) 分别为读和写

42
os.popen(command[, mode[, bufsize]])
从一个 command 打开一个管道

43
os.read(fd, n)
从文件描述符 fd 中读取最多 n 个字节，返回包含读取字节的字符串，文件描述符 fd对应文件已达到结尾, 返回一个空字符串。

44
os.readlink(path)
返回软链接所指向的文件

45
os.remove(path)
删除路径为path的文件。如果path 是一个文件夹，将抛出OSError; 查看下面的rmdir()删除一个 directory。

46
os.removedirs(path)
递归删除目录。

47
os.rename(src, dst)
重命名文件或目录，从 src 到 dst

48
os.renames(old, new)
递归地对目录进行更名，也可以对文件进行更名。

49
os.rmdir(path)
删除path指定的空目录，如果目录非空，则抛出一个OSError异常。

50
os.stat(path)
获取path指定的路径的信息，功能等同于C API中的stat()系统调用。

51
os.stat_float_times([newvalue])
决定stat_result是否以float对象显示时间戳

52
os.statvfs(path)
获取指定路径的文件系统统计信息

53
os.symlink(src, dst)
创建一个软链接

54
os.tcgetpgrp(fd)
返回与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组

55
os.tcsetpgrp(fd, pg)
设置与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组为pg。

56
os.tempnam([dir[, prefix]])
Python3 中已删除。返回唯一的路径名用于创建临时文件。

57
os.tmpfile()
Python3 中已删除。返回一个打开的模式为(w+b)的文件对象 .这文件对象没有文件夹入口，没有文件描述符，将会自动删除。

58
os.tmpnam()
Python3 中已删除。为创建一个临时文件返回一个唯一的路径

59
os.ttyname(fd)
返回一个字符串，它表示与文件描述符fd 关联的终端设备。如果fd 没有与终端设备关联，则引发一个异常。

60
os.unlink(path)
删除文件路径

61
os.utime(path, times)
返回指定的path文件的访问和修改的时间。

62
os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
输出在文件夹中的文件名通过在树中游走，向上或者向下。

63
os.write(fd, str)
写入字符串到文件描述符 fd中. 返回实际写入的字符串长度
'''





######Python3 错误和异常
print("\n\n~~~~~~~~~~~~~~~~~~~~~Python3 错误和异常~~~~~~~~~~~~~~~~~~~~~")
'''
作为Python初学者，在刚学习Python编程时，经常会看到一些报错信息，在前面我们没有提及，这章节我们会专门介绍。
Python有两种错误很容易辨认：语法错误和异常。

语法错误
Python 的语法错误或者称之为解析错，是初学者经常碰到的

异常
即便Python程序的语法是正确的，在运行它的时候，也有可能发生错误。运行期检测到的错误被称为异常。
大多数的异常都不会被程序处理，都以错误信息的形式展现.
'''

## 异常处理
print("\n\n=====异常处理=====")
'''
try语句按照如下方式工作:
首先，执行try子句（在关键字try和关键字except之间的语句）
如果没有异常发生，忽略except子句，try子句执行后结束。
如果在执行try子句的过程中发生了异常，那么try子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，那么对应的except子句将被执行。最后执行 try 语句之后的代码。
如果一个异常没有与任何的except匹配，那么这个异常将会传递给上层的try中。

一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行，如：
except OSError as err:
    ...
except ValueError:
    ...
    
处理程序将只针对对应的try子句中的异常进行处理，而不是其他的 try 的处理程序中的异常。
一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组，如：
except (RuntimeError, TypeError, NameError):
...

try except 语句还有一个可选的else子句，如果使用这个子句，那么必须放在所有的except子句之后。这个子句将在try子句没有发生任何异常的时候执行.
使用 else 子句比把所有的语句都放在 try 子句里面要好，这样可以避免一些意想不到的、而except又没有捕获的异常。
'''
import sys
try:
    f = open(filePath)
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:#最后一个except子句可以忽略异常的名称，它将被当作通配符使用。你可以使用这种方法打印一个错误信息，然后再次把异常抛出。
    print("Unexpected error:", sys.exc_info()[0])
    raise#再次把异常抛出
for arg1 in [filePath, filePath2, "abc"]:
    try:
        f = open(arg1, 'r')
    except IOError:
        print('cannot open:', arg1)
    else:
        print(arg1, 'has', len(f.readlines()), 'lines')
        f.close()
'''
异常处理并不仅仅处理那些直接发生在try子句中的异常，而且还能处理子句中调用的函数（甚至间接调用的函数）里抛出的异常。例如:
'''
def this_fails():
    x = 1/0
try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)

## 抛出异常
print("\n\n=====抛出异常=====")
'''
Python 使用 raise 语句抛出一个指定的异常。
'''
# raise NameError('HiThere')# 这样不会执行下面语句
# print("Python 使用 raise 语句抛出一个指定的异常。")
'''
raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）。
如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的 raise 语句就可以再次把它抛出。
'''
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    # raise#再次把异常抛出

## 用户自定义异常
print("\n\n=====用户自定义异常=====")
'''
你可以通过创建一个新的exception类来拥有自己的异常。异常应该继承自 Exception 类，或者直接继承，或者间接继承.
'''
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred, value:', e.value)
'''
在这个例子中，类 Exception 默认的 __init__() 被覆盖。
当创建一个模块有可能抛出多种不同的异常时，一种通常的做法是为这个包建立一个基础异常类，然后基于这个基础类为不同的错误情况创建不同的子类:
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message
'''

## 定义清理行为
print("\n\n=====定义清理行为=====")
'''
try 语句还有另外一个可选的子句finally，它定义了无论在任何情况下都会执行的清理行为。
'''
try:
    raise KeyboardInterrupt
except:
    print('except')
finally:
    print('finally')
def divide1(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    except Exception as err:
        print("other exception:", err)
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
divide1(2, 1)
divide1(2, 0)
divide1("2", "1")
'''
预定义的清理行为
一些对象定义了标准的清理行为，无论系统是否成功的使用了它，一旦不需要它了，那么这个标准的清理行为就会执行。
这面这个例子展示了尝试打开一个文件，然后把内容打印到屏幕上:
for line in open("myfile.txt"):
    print(line, end="")
以上这段代码的问题是，当执行完毕后，文件会保持打开状态，并没有被关闭。
关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法:
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
以上这段代码执行完毕后，就算在处理过程中出问题了，文件 f 总是会关闭。
'''





###### Python3 面向对象
print("\n\n~~~~~~~~~~~~~~~~~~~~~Python3 面向对象~~~~~~~~~~~~~~~~~~~~~")
''''
Python中的类提供了面向对象编程的所有基本功能：类的继承机制允许多个基类，派生类可以覆盖基类中的任何方法，方法中可以调用基类中的同名方法。
对象可以包含任意数量和类型的数据。

类定义
语法格式如下：
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
'''

## 类对象
print("\n\n=====类对象=====")
'''
类对象支持两种操作：属性引用和实例化。
属性引用使用和 Python 中所有的属性引用一样的标准语法：obj.name。
类对象创建后，类命名空间中所有的命名都是有效属性名。
'''
class MyClass:
    """一个简单的类实例"""
    i = 12345
    def f(self):
        return 'hello world'
# 实例化类
x = MyClass()
# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())

## 类的方法
print("\n\n=====类的方法=====")
'''
1
在类地内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例。

2
很多类都倾向于将对象创建为有初始状态的。因此类可能会定义一个名为 __init__() 的特殊方法（构造方法），像下面这样：
def __init__(self):
    self.data = []
类定义了 __init__() 方法的话，类的实例化操作会自动调用 __init__() 方法。所以在下例中，可以这样创建一个新的实例:
x = MyClass()
 __init__() 方法可以有参数，参数通过 __init__() 传递到类的实例化操作上。
'''
class Test1:
    def prt(self, x):
        print(x)
        print(self)
        print(self.__class__)
t = Test1()
t.prt(3)
'''
从执行结果可以很明显的看出，self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类。
self 不是 python 关键字，我们把他换成其他名称也是可以正常执行的:
'''
class Test1:
    def prt(abc, x):
        print(x)
        print(abc)
        print(abc.__class__)

t = Test1()
t.prt(4)
class Complex1:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex1(3.0, -4.5)
print(x.r, x.i)

## 继承
print("\n\n=====继承=====")
'''
Python 同样支持类的继承，如果一种语言不支持继承，类就没有什么意义。派生类的定义如下所示:
class DerivedClassName(BaseClassName1):
    <statement-1>
    .
    .
    .
    <statement-N>
需要注意圆括号中基类的顺序，若是基类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找基类中是否包含方法。
BaseClassName（示例中的基类名）必须与派生类定义在一个作用域内。除了类，还可以用表达式，基类定义在另一个模块中时这一点非常有用:
class DerivedClassName(modname.BaseClassName):
'''
#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
#单继承示例
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的构函
        people.__init__(self,n,a,w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
s = student('ken',10,60,3)
s.speak()
# 多继承
'''
Python同样有限的支持多继承形式。多继承的类定义形如下例:
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法。
'''
#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
#单继承示例
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的构函
        people.__init__(self,n,a,w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
#另一个类，多重继承之前的准备
class speaker1():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))
#多重继承
class sample1(student,speaker1):
    a =''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker1.__init__(self,n,t)
test = sample1("Tim",25,80,4,"Python")
test.speak()   #方法名同，默认调用的是在括号中排前地父类的方法
#方法重写
'''
如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法.
'''
class Parent:        # 定义父类
    def myMethod(self):
        print ('调用父类方法')
class Child(Parent): # 定义子类
    def myMethod(self):
        print ('调用子类方法')
c = Child()          # 子类实例
c.myMethod()         # 子类调用重写方法
super(Child,c).myMethod() #super() 函数是用于调用父类(超类)的一个方法。用子类对象调用父类已被覆盖的方法.

## 类属性与方法
print("\n\n=====类属性与方法=====")
'''
类的私有属性
__private_attrs：两个下划线开头，声明该属性为私有，不能在类地外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。

类的私有方法
__private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类地外部调用。self.__private_methods。

类的专有方法：
__init__ : 构造函数，在生成对象时调用
__del__ : 析构函数，释放对象时使用
__repr__ : 打印，转换
__setitem__ : 按照索引赋值
__getitem__: 按照索引获取值
__len__: 获得长度
__cmp__: 比较运算
__call__: 函数调用
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__div__: 除运算
__mod__: 求余运算
__pow__: 乘方
'''
class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量
    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print (self.__secretCount)
counter = JustCounter()
counter.count()
counter.count()
print (counter.publicCount)
# print (counter.__secretCount)  # 报错，实例不能访问私有变量
class Site:
    def __init__(self, name, url):
        self.name = name       # public
        self.__url = url   # private
    def who(self):
        print('name  : ', self.name)
        print('url : ', self.__url)
    def __foo(self):          # 私有方法
        print('这是私有方法')
    def foo(self):            # 公共方法
        print('这是公共方法')
        self.__foo()
x = Site('菜鸟教程', 'www.runoob.com')
x.who()        # 正常输出
x.foo()        # 正常输出
# x.__foo()      # 报错
# 运算符重载
'''
Python同样支持运算符重载，我们可以对类的专有方法进行重载，下例是对加运算__add__进行重载：
'''
class Vector1:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)
    def __add__(self,other):
        return Vector1(self.a + other.a, self.b + other.b)
v1 = Vector1(2,10)
v2 = Vector1(5,-2)
print (v1 + v2)





###### Python3 标准库概览
print("\n\n~~~~~~~~~~~~~~~~~~~~~Python3 标准库概览~~~~~~~~~~~~~~~~~~~~~")
'''
操作系统接口
os模块提供了不少与操作系统相关联的函数。

文件通配符
glob模块提供了一个函数用于从目录通配符搜索中生成文件列表.

命令行参数
通用工具脚本经常调用命令行参数。这些命令行参数以链表形式存储于 sys 模块的 argv 变量。

错误输出重定向和程序终止
sys 还有 stdin，stdout 和 stderr 属性，即使在 stdout 被重定向时，后者也可以用于显示警告和错误信息。

字符串正则匹配
re模块为高级字符串处理提供了正则表达式工具。对于复杂的匹配和处理，正则表达式提供了简洁、优化的解决方案.

数学
math模块为浮点运算提供了对底层C函数库的访问.
random提供了生成随机数的工具。

访问 互联网
有几个模块用于访问互联网以及处理网络通信协议。其中最简单的两个是用于处理从 urls 接收的数据的 urllib.request 以及用于发送电子邮件的 smtplib.

日期和时间
datetime模块为日期和时间处理同时提供了简单和复杂的方法。
支持日期和时间算法的同时，实现的重点放在更有效的处理和格式化输出。
该模块还支持时区处理.

数据压缩
以下模块直接支持通用的数据打包和压缩格式：zlib，gzip，bz2，zipfile，以及 tarfile。

性能度量
有些用户对了解解决同一问题的不同方法之间的性能差异很感兴趣。Python 提供了一个度量工具，为这些问题提供了直接答案。
例如，使用元组封装和拆封来交换元素看起来要比使用传统的方法要诱人的多,timeit 证明了现代的方法更快一些。
相对于 timeit 的细粒度，:mod:profile 和 pstats 模块提供了针对更大代码块的时间度量工具。

测试模块
开发高质量软件的方法之一是为每一个函数开发测试代码，并且在开发过程中经常进行测试
doctest模块提供了一个工具，扫描模块并根据程序中内嵌的文档字符串执行测试。
测试构造如同简单的将它的输出结果剪切并粘贴到文档字符串中。
通过用户提供的例子，它强化了文档，允许 doctest 模块确认代码的结果是否与文档一致.
unittest模块不像 doctest模块那么容易使用，不过它可以在一个独立的文件里提供一个更全面的测试集.
'''




###### Python3 实例
print("\n\n~~~~~~~~~~~~~~~~~~~~~Python3 实例~~~~~~~~~~~~~~~~~~~~~")
'''
以下实例在 Python3.4.3 版本下测试通过：
Python Hello World 实例
Python 数字求和
Python 平方根
Python 二次方程
Python 计算三角形的面积
Python 随机数生成
Python 摄氏温度转华氏温度
Python 交换变量
Python if 语句
Python 判断字符串是否为数字
Python 判断奇数偶数
Python 判断闰年
Python 获取最大值函数
Python 质数判断
Python 输出指定范围内的素数
Python 阶乘实例
Python 九九乘法表
Python 斐波那契数列
Python 阿姆斯特朗数
Python 十进制转二进制、八进制、十六进制
Python ASCII码与字符相互转换
Python 最大公约数算法
Python 最小公倍数算法
Python 简单计算器实现
Python 生成日历
Python 使用递归斐波那契数列
Python 文件 IO
Python 字符串判断
Python 字符串大小写转换
Python 计算每个月天数
Python 获取昨天日期
Python list 常用操作
'''




###### Python CGI编程
print("\n\n~~~~~~~~~~~~~~~~~~~~~Python CGI编程~~~~~~~~~~~~~~~~~~~~~")








'''
print("\n\n~~~~~~~~~~~~~~~~~~~~~***~~~~~~~~~~~~~~~~~~~~~")
print("\n\n=====***=====")
'''
