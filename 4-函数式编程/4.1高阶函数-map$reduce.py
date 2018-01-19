# coding=utf-8

list1 = [1, 2, 3, 4]
# map()：将传入的函数依次作用到序列到每一个元素
print 'map():'
def f(x):
    return x*x
print map(f, list1)

print map(str, list1)

# reduce()：reduce把一个函数作用在一个序列[x1, x2, x3...]上，并把结果继续和序列的下一个元素做累积计算
print '\nreduce():'
def add(x,y):
    return x+y
print reduce(add, list1)     # 相当于sum()函数
print ''

# 组合题：写一个str2int函数：
str = '98723954'
def char2num(ch):
    dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    #print dict[ch]
    return dict[ch]
def str2int(s):
    def fn(x,y):
        return x*10 + y
    return reduce(fn, map(char2num, s))
print str2int(str)
print '这里可以将fn函数改写成lambda表达式为：'

def str2int(s):
    return reduce(lambda x,y:x*10+y, map(char2num, s))
print str2int(str)

# 练习一：利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
#   输入：['adam', 'LISA', 'barT']，
#   输出：['Adam', 'Lisa', 'Bart']。
l = ['adam', 'LISA', 'barT']
def fn(str):
    return str[0].upper()+str[1:].lower()
print map(fn, l)


# 练习二：编写一个prod()函数，可以接受一个list并利用reduce()求积。
def mul(x,y):
    return x*y
print reduce(mul, list1)

