# -*- coding: utf-8 -*-
# @Time    : 2024/4/13 9:33 下午
# @Author  : Hoey


# 读取 tmp.txt 中的数据并打印
def read_file(file_path):
    # 读取file_path, r: read
    file = open(file_path, 'r')
    result = ''
    for line in file:
        # 第一次进来， line =  123 ; result = line
        # 第二进来，  line = 456 ; result = 123; result = 123456
        result = result + line

    return result


# 写文件 1. 覆盖写入 2
# file_path: 代表是我要写入到哪个文件
# content: 代表是我要写入的内容
def write_1(file_path, content):
    # r : read(读) , a: append（追加）, w: write(覆盖)
    file = open(file_path, 'w', encoding='UTF-8')
    file.write(content)
    # 从内存中写入到磁盘
    file.flush()
    # 关闭文件释放资源
    file.close()

def write_2(file_path, content):
    file = open(file_path, 'a', encoding='UTF-8')
    file.write(content)
    file.flush()
    file.close()



if __name__ == '__main__':
    # result = read_file('/Users/hoey/workspace/pycharm/learn_python/day03/tmp.txt')
    # print(result)

    file_path = '/Users/hoey/workspace/pycharm/learn_python/day03/tmp.txt'
    msg = 'asdasdasdasdas\n'
    write_2(file_path, msg)
    msg1 = 'hahahah\n'
    write_2(file_path, msg1)