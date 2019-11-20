"""
Python的内置函数
- 数学相关: abs / divmod / pow / round / min / max / sum
- 序列相关: len / range / next / filter / map / sorted / slice / reversed
- 类型转换: chr / ord / str / bool / int / float / complex / bin / oct / hex
- 数据结构: dict / list / set / tuple
- 其他函数: all / any / id / input / open / print / type

Version: 0.1
Author: 骆昊
Date: 2018-03-05
"""


def myfilter(mystr):
    return len(mystr) == 6


# help()
print(chr(0x9a86))
print(hex(ord('骆')))       #转换一个整数对象为十六进制的字符串表示
print(abs(-1.2345))
print(round(-1.2345))       #round返回浮点数x的四舍五入值
print(pow(1.2345, 5))       #pow()返回x^y的值
fruits = ['orange', 'peach', 'durian', 'watermelon']
print(fruits[slice(1, 3)])
#slice()函数实现切片对象,slice(1, 3)截取第二个和第三个元素
fruits2 = list(filter(myfilter, fruits))
#filter()函数用于过滤序列,过滤掉不符合条件的元素,返回符合条件元素组成的列表
print(fruits)
print(fruits2)
