#coding:utf-8

# Python内置的sorted()函数就可以对list进行排序：

# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。

# 忽略大小写来比较两个字符串:
def cmp_ignore_case(s1, s2):
    u1 = s1.upper();
    u2 = s2.upper();
    if u1 > u2:
        return 1
    elif u1 < u2:
        return -1
    else:
        return 0

list1 = ['bob', 'about', 'Zoo', 'Credit']
print sorted(list1)
print sorted(list1, cmp_ignore_case)