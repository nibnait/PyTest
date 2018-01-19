# coding=utf-8

#1. 列表生成式可直接转换成生成器
L = [x*x for x in range(10)]
print L

g = (x*x for x in range(10))
print g
for gg in g:
    print gg,
print

#2. 若推算算法比较复杂，可以用函数来实现
def fib(max):
    n,a,b = 0,0,1
    while n<max:
        # print b
        yield b #生成器的标志，相当于函数里的return
        a,b = b, a+b
        n += 1
print fib
for n in fib(6):
    print n,

