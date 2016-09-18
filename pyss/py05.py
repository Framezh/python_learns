#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# 高级特性
# 
def func():
    L = []
    n = 1
    while n <= 99:
        L.append(n)
        n += 2
    print(L)

# 切片
def func1():
    L = ['aa', 'bb', 'cc']
    # L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3;
    # 即索引0，1，2，正好是3个元素;
    L[0:2]
    L[:2]
    L[-3:-1]
    print(L[-3:])
    S = list(range(0,100,5))
    print(S)
def func2():
    L = list(range(100))
    # print("1. ", L[:10])
    # print('2. ', L[-10:])
    print('3. ', L[10:20])
    print('4. ', L[:10:2]) # 前10个数，每两个取一个;
    print('5. ', L[::5]) # 所有数，每5个取一个;
    # print('6. ', L[:]) # 只写[:]就可以原样复制一个list
    print('6. ', (1,2,3,4,5)[:3]) # tuple
    print('7. ', 'ABCDEF'[:3]) # string
###
### Python没有针对字符串的截取函数，只需要切片一个操作就可以完成，非常简单;

# 迭代
def func3():
    # dict 
    d = {'a': 12, 'b': 13, 'c': 14}
    for i in d:# 默认迭代key
        print('key 迭代：', i)
    for val in d.values():# 迭代value
        print('value 迭代：', val)
    for key, val in d.items():# 迭代key ,value
        print('key,value迭代：', key, val)
    str = 'ABCDEF'
    for s in str:
        print('字符串迭代：', s)
# 
# 判断对象是可迭代对象：通过collections模块的Iterable类型判断;


#
# 主程序
if __name__ == '__main__':
    # 
    func3()
    # func2()
    # 
    # func1()
    # 
    # func()

    