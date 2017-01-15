#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# 函数式编程
#

### 1. 高阶函数
# 函数名其实就是指向函数的变量
# 传入函数;
# 编写高阶函数，就是让函数的参数能够接收别的函数;
def funf(a, b, f):
    return f(a)+f(b)

# a. map() / reduce
def f(x): # f(x) = x*x
    return x*x
# 序列求和
def g(x, y):
    return x+y
def gx(x, y):
    return x * 10 + y
# b. filter
# c. sorted


### 2. 返回函数

### 3. 匿名函数

### 4. 装饰器

### 5. 偏函数


#
### 主程序
if __name__ == '__main__':
    # a = funf(-2, -5, abs)
    # print(a)
    ### map()的用法
    ss = [1, 2, 3, 4, 5]
    # arg = map(str, ss)
    # arg2 = map(f, ss)
    # print('arg:', list(arg), '\narg2:', list(arg2))
    ### reduce(x, y)用法: 序列求和
    from functools import reduce
    sa = reduce(g, ss)
    print(sa) # 求和
    sb = reduce(gx, ss)
    print(sb) # 数字变换