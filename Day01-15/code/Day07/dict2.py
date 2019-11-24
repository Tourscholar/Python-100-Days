"""
字典的常用操作

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def main():
    stu = {'name': '骆昊', 'age': 38, 'gender': True}
    print(stu)
    print(stu.keys())
    print(stu.values())
    print(stu.items())
    #items()函数以列表返回可遍历的(键,值)元组数组
    for elem in stu.items():
        print(elem)
        print(elem[0], elem[1])
    if 'age' in stu:
        stu['age'] = 20
    print(stu)
    stu.setdefault('score', 60)
    #setdefault()函数和get()函数类似,如果键不存在于字典中,将会添加键并将值设为默认值
    print(stu)
    stu.setdefault('score', 100)
    print(stu)
    stu['score'] = 100
    print(stu)


if __name__ == '__main__':
    main()
