# -*- coding: utf-8 -*-
# @Time    : 2024/3/23 10:06 下午
# @Author  : Hoey


def set_test():
    """
    一批数据，去重存储场景，无序
    """
    arr_set = {'a', 'b', 'c', 'a'}
    for s in arr_set:
        print(s)


if __name__ == '__main__':
    arr_set = {'a', 'b', 'c', 'a'}

    for s in arr_set:
        print(s)


    # x y z 无须
    # arr_set2 = set()
    # arr_set2.add('x')
    # arr_set2.add('y')
    # arr_set2.add('y')
    # arr_set2.add('z')
    # arr_set2.add('z')
    # for s in arr_set2:
    #     print(s)

    # # 有序
    # arr_list = list()
    # arr_list.append('x')
    # arr_list.append('z')
    # arr_list.append('x')
    # arr_list.append('y')
    # arr_list.append('z')
    # for s in arr_list:
    #     print(s)















