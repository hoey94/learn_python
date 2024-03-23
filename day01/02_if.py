# -*- coding: utf-8 -*-
# @Time    : 2024/3/23 8:55 下午
# @Author  : Hoey
import random


def if_while_test():
    r_num = random.randint(1, 100)
    flag = True
    while flag:
        num = int(input("请你输入一个0~100的数字:"))
        if num == r_num:
            print("成功匹配到数字")
            flag = False
        elif num > r_num:
            print("输入的数字太大了")
        elif num < r_num:
            print("输入的数字太小了")

if __name__ == '__main__':
    if_while_test()
