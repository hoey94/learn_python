# -*- coding: utf-8 -*-
# @Time    : 2024/4/13 8:49 下午
# @Author  : Hoey


def say():
    # print(123)
    return 123

def say_1(a):
    print(a)

# 非可变参数
def say_2(name, age):
    print(f'name: {name}')
    print(f'age: {age}')



l_dict = {'zs': 'shanghai', 'ls': 'shenzhen'}

def say_3(name='zs'):
    # 每当来一个name，返回出他的信息
    address = l_dict[name]
    return name, address


# 可变参数1: 当不确定要传递几个参数的时候
# arguments: 参数
# say_4('zs', 19)
tpl = ('a', 'b', 'c')
def say_4(*args):
    print(type(args)) # tuple
    for arg in args:
        print(arg)

# 可变参数2: 在不确定要传递多少个参数时，使用
# say_5(name='zs', age=19)
def say_5(**args):
    print(type(args)) # dict
    for k in args:
        print(f"key: %s value: %s" % (k, args[k]))


# 计算两个数相加
def jiafa(a, b):
    return a + b

# 计算两个数相乘
def chengfa(a, b):
    return a * b

def my_print(func):
    print(func(1,2))


# 数据类型 : 字符串: String、 列表：List 、 元组:Tuple、 字典: Dict、 函数: function、 数字: int、float


if __name__ == '__main__':
    my_print(jiafa)
    my_print(chengfa)







    # 一个等
    # asd = say()
    # print(asd)
    # a = 1
    # say_1('hello')
    # print(a)

    # say_2('zs', 19)
    # say_2(age=19, name='zs')

    # name, address = say_3('ls')
    # print(f'name: {name}, address: {address}')

    #
    # address = say_3('ls')
    # print(address)
    # say_4('zs', 'shanghai', 19)

    # say_5(name='zs', age=19)

