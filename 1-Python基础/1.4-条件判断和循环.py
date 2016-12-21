# coding=utf-8
import sys

age = 18
if age>18:
    print '成年人'
elif age>14:
    print '青少年'
else:
    print '儿童'

# 循环
list = [1,2,3,4]
for l in list:
    print l,
print

# range
for l in range(5):
    print l,
print

# while循环
sum = 0
n = 5
while n>0:
    sum += n
    n -= 1

print sum

# raw_input
birth = int(raw_input())
if birth>2000:
    print "00后"
else:
    print "00前"