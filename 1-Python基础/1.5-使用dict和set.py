# coding=utf-8

# 在Python中，字符串、整数等都是不可变的，因此，可以放心地作为dict的key。而list是可变的，就不能作为key：

dictionary={'a':1, 'b':2, 'c':3}
print dictionary['a']

if 'c' in dictionary:
    print dictionary['c']

print dictionary.get('c', 4)
print dictionary.get('d', 4)
print dictionary

dictionary.pop('c')
print dictionary

# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
# 要创建一个set，需要提供一个list作为输入集合：
s = set([1,2,3])
print s
s.add(2)
print s
s.add(4)
print s
s.remove(1)
print s

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1,2,3,4])
s2 = set([3,4,5,6])
print s1 & s2

# test 将tuple放入set中
#   t = (1,2,[3,4])    显然不行，因为t[2]是一个list，是可变的
t = (1,2,3)
s = set(t)
print s