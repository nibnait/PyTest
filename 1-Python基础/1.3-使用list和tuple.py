# coding=utf-8

# list
#   Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
list1 = ['a', 2, 'c', 'd']

print list1[0]

print list1

print len(list1)


# 获取倒数第一个元素
print list1[-1]

# append 向数组末尾追加元素
list1.append('x')
print list1

# 向指定位置插入元素
list1.insert(1, 'aa')
print list1

# 删除末尾元素
list1.pop()
print list1

# 删除指定位置元素
list1.pop(-1)
print list1

# tuple
#   另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改

# 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t = (1,)
print t

# 如果tuple中包含一个list元素，则list里面的东西还是可变的。
t=(1,2,['a','b'],4)
print t
t[2][0] = 3
print t
