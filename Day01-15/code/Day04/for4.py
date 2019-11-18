"""
输入一个正整数判断它是不是素数

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""
from math import sqrt   #sqrt(x)函数返回数字x的平方根

num = int(input('请输入一个正整数: '))
end = int(sqrt(num))
is_prime = True
if num == 1:
    is_prime = False
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime == True:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)
