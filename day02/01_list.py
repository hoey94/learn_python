# -*- coding: utf-8 -*-
# @Time    : 2024/3/23 9:11 下午
# @Author  : Hoey


if __name__ == '__main__':
    # list的使用
    # a = 1
    # b = 2
    # c = 3
    # my_l = []
    # my_l.append(a)
    # my_l.append(b)
    # my_l.append(c)
    # print(my_l)
    # print(type(my_l))

    # 1. 元素的位置  0 1 2 3 4
    # 2. 元素的值    1 2 3 4
    # my_l = [1, 2, 3]
    # print(my_l)
    # print(type(my_l))
    # for i in my_l:
    #     print(i)
    # 增加值
    # my_l.append(4)
    # print(my_l)
    # my_l.remove(1)
    # print(my_l)
    # my_l.index(2)

    # 爱 = 1
    # print(f'爱{爱}')

    # my_l = [1, 2, 3]
    # for index, i in enumerate(my_l):
    #     print(f'位置{index}:值是{i}')

    my_l = [1, 2, 3]
    # 位置变量
    # index = 0
    # 集合的总长度 3
    # length = len(my_l)
    # 1. 如果使用while，终止条件是什么？
    # 位置小于3或者小于等于2的时候  进行循环
    # 位置      3或者是2
    # 当位置 < 3 length的时候进行循环
    # 当位置 <= 2(length-1)的时候进行循环
    # while index < length:
    #     print(f'位置{index}:值是{my_l[index]}')
    #     # 每循环一次，代表当前位置已经被检索，需要更新下一次要打印的位置。
    #     index += 1 # index = index + 1

    # 0的含义是位置， 2的含义是值， 指定一个位置放入值
    # my_l.insert(0, 2)

    s = my_l[0:2]
    print(s)



def list_test():
    """
    一批数据，可修改、可重复的存储场景
    """
    arr = ['a', 'b', 'c']
    for a in arr:
        print(f"列表:{a}")

    index = 0
    while index < len(arr):
        print(f"列表:{arr[index]}")
        index += 1


