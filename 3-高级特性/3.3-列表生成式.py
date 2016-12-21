# coding=utf-8

# 一行代码 生成你想要的list

print [x*x for x in range(1,11) if x%2==0]

# 双重for循环，生成全排列
print [m+n for m in 'ABC' for n in 'XYZ']

# 列出当前目录下的所有文件名
import os
print [d for d in os.listdir('.')]      #直接打印列表  中文一般是显示u"\x1234"
for d in os.listdir('.'):
    print d     # 没毛病。

# 思考题：
L = ['Hello', 'World', 18, 'Apple', None]
# print [x.lower() for x in L if isinstance(x, str)]
print [x.lower() if isinstance(x, str) else x for x in L]
# print map(lambda x : x.lower() if isinstance(x, str) else x, L)