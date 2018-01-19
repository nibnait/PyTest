# coding=utf-8

# list、tuple都可以进行切片操作

l = range(100)

print l[0:3]
print l[:3]
print l[1:3]
print l[-3:]

# 前10个数 每2个取一个：
print l[0:10:2]     # start,end,step
# 所有数 每5个娶一个
print l[::5]