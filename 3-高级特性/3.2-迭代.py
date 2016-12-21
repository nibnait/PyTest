# coding=utf-8

# dict：for循环默认key
d = {'a':1, 'b':2, 'c':3}
for key in d:
    print key,
print
# 迭代value：
for value in d.itervalues():
    print value,
print ''
# 同时迭代key和value
for k,v in d.iteritems():
    print k,v
print

#Q1：如何判断一个对象是否可迭代？
from collections import Iterable
l = [1,2,3,4]
print isinstance(l, Iterable)
print

#Q2：如何实现Java那种的带下标的循环？
for i,value in enumerate(l):
    print i, value
print

#A1:for循环里，同时引用了两个变量，在Python里是很常见的
ll = ((1,2),(3,4),(5,6))
ll = [(1,2),(3,4),(5,6)]
for x,y in ll:
    print x,y