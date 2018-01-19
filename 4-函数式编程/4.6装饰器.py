# coding:utf-8

import time
import datetime
# 1。每个函数都是一个对象
def hello():
        print ("hello,world");


if __name__ == "__main__":
        hello();

# 2。内置函数 以及域

def say():
    def say_hello():
        print("hello,world~!")
        # return "1"

    return say_hello

print say
print say()
print say()()

a = say()();

print a

# 3。参数（函数）传递

def say(func_word):
    func_word()

say(hello)


print '------------------------'
# 4. 装饰器

# 装饰一下hello函数【装饰器：people_say】
def people_say(func):
    def say():
        print("begin at "+ str(time.time()))
        func()
        print ("end at." + str(time.time()))
    return say

chang = people_say(hello)
chang()


print '------------------------'
@people_say
def he():
    print("hello,world!")

he();

#---------------------------------------------------
#5. 多层装饰器
