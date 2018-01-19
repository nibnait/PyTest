# coding:utf-8

#from functools import partial
import functools

def say(word):
    print(word)

# 参数缓存
say_hello = functools.partial(say, word="hello")

say("hello")
say_hello


#### 偏函数（partial） 其实就是参数缓存