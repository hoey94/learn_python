# -*- coding: utf-8 -*-
# @Time    : 2024/3/23 9:52 下午
# @Author  : Hoey


def string_test():
    str1 = "hoey.tk"
    s = str1.split(".")[1]
    print("域名的后缀为:\%%s\%" % (s))

    str2 = "blog.hoey.tk"
    index = str2.index("hoey")
    domain = str2[index:]
    print("域名为: %s" % domain)

    str3 = "insert into %s" % "t1"
    print(str3)
    return None







if __name__ == '__main__':
    # str = 'abxkjasld'
    #
    # for s in str:
    #     print(s)

    # str_2 = 'my home in china'
    # l_list = str_2.split(' ')
    # print(l_list)


    # str_2 = 'my home in china'
    # for s in str_2:
    #     print(s)
    #
    # index = str_2.index('in')
    # print(index)

    str2 = "blog.hoey.tk"
    index = str2.index("hoey")
    # print(index)
    # (5 - len(str2))
    # --> hoey.tk  blog.不要了
    domain = str2[index: len(str2)]
    domain = str2[index:]
    # domain = str2[5, 7]
    print("域名为: %s" % domain)








    # print('hello')
    # a = 1
    # print(f'hello {a}')
    # print('hello %s' % a)
    #
    # hhh = '你好'
    # print('hello %s' % hhh)









