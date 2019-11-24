"""
定义和使用列表
- 用下标访问元素
- 添加元素
- 删除元素

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def main():
    fruits = ['grape', '@pple', 'strawberry', 'waxberry']
    print(fruits)
    # 通过下标访问元素
    print(fruits[0])
    print(fruits[1])
    print(fruits[-1])
    print(fruits[-2])
    # print(fruits[-5]) # IndexError
    # print(fruits[4])  # IndexError
    fruits[1] = 'apple'
    print(fruits)
    # 添加元素
    fruits.append('pitaya')
    #insert()函数用于将指定对象插入列表的指定位置
    fruits.insert(0, 'banana')
    print(fruits)
    # 删除元素
    del fruits[1]
    fruits.pop()
    fruits.pop(0)
    #remove()函数移除列表中指定的值
    fruits.remove('apple')
    print(fruits)


if __name__ == '__main__':
    main()
