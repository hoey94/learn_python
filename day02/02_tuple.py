# -*- coding: utf-8 -*-
# @Time    : 2024/3/23 9:46 下午
# @Author  : Hoey



def tuple_test():
    """
    一批数据，不可修改、可重复的存储场景
    """
    # tpl = ('a',)
    tpl = ('a', 'b', 'c')
    for t in tpl:
        print(f"元组:{t}")

    index = 0
    while index < len(tpl):
        print(f"元组:{tpl[index]}")
        index += 1


if __name__ == '__main__':
    my_tuple = ('a', 'b', 'c')
    print(my_tuple)
    print(type(my_tuple))


    for index, x in enumerate(my_tuple):
        print(f'{index}:{x}')



