# coding=utf-8

def my_abs(x):
    #1. 检查参赛类型
    if not isinstance(x, (int, float)):
        raise TypeError('参数类型错误。')
    if x >= 0:
        return x
    else:
        return -x

print my_abs(-3)
#print my_abs('a')

# 定义一个空函数：
def nop():
    pass

# 返回多个值
import math
def move(x, y, step, angle=0):
    x = x + step * math.cos(angle)
    y = y + step * math.sin(angle)
    return x, y

x,y = move(100, 100, 60, math.pi/6)
print x,y
# 其实 Python返回多个值的时候，实际返回的是一个元组,只是那样写 直接赋值起来更方便一些。
t = move(100, 100, 60, math.pi/6)
print t