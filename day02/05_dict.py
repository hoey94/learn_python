# -*- coding: utf-8 -*-
# @Time    : 2024/3/23 10:15 下午
# @Author  : Hoey

def dict_test():
    """
    一批数据,可用Key检索Value的存储场景，实际上就是Map
    """
    m_dict = {"zs": 18, "ls": 19}
    for k in m_dict:
        print(f"key: %s value: %s" % (k, m_dict[k]))

    for k in m_dict.keys():
        print(f"key: %s value: %s" % (k, m_dict[k]))

    m_dict2 = {"zs": {"英语": 80, "语文": 60}, "ls": {"英语": 55, "语文": 80}}
    for k in m_dict2:
        for kk in m_dict2[k]:
            print(f"姓名: {k} 科目: {kk} 分数: {m_dict2[k][kk]}")

    data = {'temp1': 2.31, 'temp2': 1.21}
    values = list(data.values())
    print(f'将dict转换成list{values}')

    # dict 带下标遍历
    d = {'temp1': 2.31, 'temp2': 1.21, 'temp3': 1.11, 'temp4': 1.01}
    for index, (key, value) in enumerate(d.items()):
        print(f'Index: {index}, Key: {key}, Value: {value}')


if __name__ == '__main__':

    # m_dict = {'zs': 18, 'ls': 19}
    # for key in m_dict.keys():
    #     print(key)
    #     print(m_dict[key])
    #

    m_dict = {
        '学员1': {'name': 'zs', 'age': 18, 'address': '上海'},
        '学员2': {'name': 'ls', 'age': 19, 'address': '上海'},
        '学员3': {'name': 'ww', 'age': 19, 'address': '上海'}
    }
    for key in m_dict.keys():
        print(key)
        print(m_dict[key])
        for key2 in m_dict[key].keys():
            print(key2)
            print(m_dict[key][key2])

