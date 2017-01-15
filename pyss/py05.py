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

# 1.切片
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

# 2.迭代
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
### 判断对象是可迭代对象：通过collections模块的Iterable类型判断;
from collections import Iterable
def func4():
    s = isinstance('abc', Iterable)
    ss = isinstance(123, Iterable)
    print(s, ss)
# 下标循环 enumerate
def func5():
    for i, value in enumerate(('a', 'b', 'c')):
        print(i, value)
    for x, y in [(1, 1), (2, 2), (1, 2)]:
        print('2变量迭代：', x, y)

# 3..列表生成式 (List Comprehensions)
def func6():
    print(list(range(1, 11)))
    print()
    print('生成[1x1, 2x2, 3x3, ..., 10x10]')
    L = []
    for i in range(1, 11):
        L.append(i * i)
    print(L)
    ### 列表生成式
    M = [x*x for x in range(1, 11)]
    Ma = [x*x for x in range(1, 11) if x % 2 == 0] # 加条件判断
    print('列表生成式：\n', M, '\n', Ma)
    ### 全排列
    Mb = [m + n for m in 'ABC' for n in 'abc']
    print('全排列：\n', Mb)
    ### 2个变量
    d = {'x': 'A', 'y': 'B', 'z': 'C'}
    dls = [k +'='+ v for k, v in d.items()]
    print('dls 2个变量 列表生成式:\n', dls)
### 列出当前目录下的所有文件和目录名
def funcF():# 文件列表
    import os
    dirs = [d for d in os.listdir('.')]# 列出文件和目录
    print(dirs)
### eg.
def funcEg():
    L1 = ['Hello', 'World', 18, 'Apple', None]
    lp = [x.lower() for x in L1 if isinstance(x, str)]
    up = [x.upper() for x in L1 if isinstance(x, str)]
    print(lp, '\n', up)

# 4..生成器 generator ****
### 第 1 种方法: ()
def funcg1():
    g1 = (x*x for x in range(6))
    print(g1)
    print(next(g1), ' ', next(g1), ' ', next(g1)) # 最后没有数据时,抛出StopIteration的错误;
    for n in g1:
        print(n)
### 第 2 种方法: yield
def funcg2():
    print('yield 1:')
    yield 1
    print('yield 2:')
    yield 2
    print('yield 3:')
    yield 3
    return 'demo'
### 输出斐波那契数列的前N个数
def fib(n):
    i, a, b = 0, 0, 1
    while i < n:
        print(b)
        a, b = b, a+b
        i += 1
    return 'nice'
def fib2(n):
    i, a, b = 0, 0, 1
    while i < n:
        yield b
        a, b = b, a+b
        i += 1
    return 'nice'
### 杨辉三角
def triangles():
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0]+a, a+[0])]
    print('---')
# def angles():
#     s = 1
#     tt = [1]
#     for
#     print

# 5..迭代器 ****
### 可以直接作用于for循环的对象统称为可迭代对象：Iterable;
### 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator;
def func8():
    print('----------')
    a = isinstance([], Iterable)
    b = isinstance( (x for x in range(11)), Iterable)
    c = isinstance('abc', Iterable)
    print('可迭代对象\n', a, b, c)
    print('----------')
    from collections import Iterator
    a = isinstance([], Iterator)
    b = isinstance( (x for x in range(11)), Iterator)
    c = isinstance('abc', Iterator)
    print('迭代器\n', a, b, c)
    ### Iterable 可迭代对象 变成 Iterator 迭代器对象;
    print('\n可迭代对象 -> 迭代器对象: iter()\n', isinstance(iter('abcd'), Iterator))


#
# 主程序
if __name__ == '__main__':
    #
    func8()
    
    # funcg1()
    # f = funcg2()
    ###
    # while True:
    #     try:
    #         x = next(f)
    #         print('x: ', x)
    #     except StopIteration as e: # StopIteration异常
    #         print('return value: ', e.value)
    #         break
    ###
        # fib(5)
        # print(fib2(6))
        # for x in fib2(6):
        #     print(x)
    ###
    # triangle = triangles()
    # for i in range(11):
    #     print(next(triangle))
    
    # funcEg()
    # func6()
    # funcF()
    
    # func5()
    
    # func4()
    # func3()
    # func2()
    
    # func1()
    
    # func()

    