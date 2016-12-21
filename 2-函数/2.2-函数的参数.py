# coding=utf-8

# 默认参数：尽量设置成不变的对象

def add_end(L=None):
    if L is None:
        L = []
    L.append('End')
    return L

print add_end()
print add_end()
print add_end()

# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    print sum

calc()
calc(1,2,3)
nums = (1,2,3)
calc(*nums)
nums = [1,2,3]
calc(*nums)

# 关键字参数：（可自己封装成一个dict传入）
def person(name, age, **kw):
    print 'name:',name, ', age:',age, ', other:',kw

person('aa', 11)
person('aa', 11, city='shanghai')
kw = {'city':'xian', 'job':'Engineer'}
person('bb', 22, **kw)


# 参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。
