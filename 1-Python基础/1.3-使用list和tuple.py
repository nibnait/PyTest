# coding=utf-8

# list
#   Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
list = ['a', 2,'c','d']

print list[0]

print list

print len(list)


# 获取倒数第一个元素
print list[-1]

# append 向数组末尾追加元素
list.append('x')
print list

# 向指定位置插入元素
list.insert(1,'aa')
print list

# 删除末尾元素
list.pop()
print list

# 删除指定位置元素
list.pop(-1)
print list

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
