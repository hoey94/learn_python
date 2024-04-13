# -*- coding: utf-8 -*-
# @Time    : 2024/4/13 10:11 下午
# @Author  : Hoey


def main():
    print('run1 ....')
    try:
        i = 1 / 0
    except Exception as e:
        print('在这里干自己想干的事情')
        # 记录异常
        # 忽略异常
        print(e)

    print('run2 ....')


if __name__ == '__main__':
    main()