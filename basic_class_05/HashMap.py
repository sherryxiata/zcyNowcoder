#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 9:34
# @Author  : wenlei

'''
哈希表操作
'''

map = []
map['zuo'] = '31'                     # 添加

print(map.__contains__('zuo'))        # 检查key是否存在
print(map.__contains__('chengyun'))
print('=========================')

print(map.get('zuo'))                 # 获取value值
print(map.get('chengyun'))
print('=========================')

print(not map)                        # map是否为空
print(len(map))                       # map的大小
print('=========================')

print(map.pop('zuo'))                 # 删除，会返回value
print(map.__contains__('zuo'))
print(map.get('zuo'))
print(not map)
print(len(map))
print('=========================')

map['zuo'] = '31'
print(map.get('zuo'))
map['zuo'] = '32'                      # 修改
print(map.get('zuo'))
print('=========================')

map['zuo'] = '31'
map['cheng'] = '32'
map['yun'] = '33'

for key in map.keys():                 # 打印key
    print(key)
print('=========================')

for value in map.values():             # 打印value
    print(value)
print('=========================')

map.clear()                            # 清空
map['A'] = '1'
map['B'] = '2'
map['C'] = '3'
map['D'] = '1'
map['E'] = '2'
map['F'] = '3'
map['G'] = '1'
map['H'] = '2'
map['I'] = '3'

for key, value in map.items():          # 打印键值对
    print(key, value)
print('=========================')

# for key, value in map.items():          # 报错！不能在可迭代对象中删除元素
#     if not value == '1':
#         map.pop(key)

removeKeys = []
for key, value in map.items():          # 批量删除：先收集，再删除
    if not value == '1':
        removeKeys.append(key)
for key in removeKeys:
    map.pop(key)

for key, value in map.items():
    print(key, value)
print('=========================')
