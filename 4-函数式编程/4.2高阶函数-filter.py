# coding=utf-8

# Python内建的filter()函数用于过滤序列。
# 和map()类似，filter()也接收一个函数和一个序列。
# 和map()不同的时，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

# 练习：filter()删除1~100的素数。
def is_prime(n):
    if (n % 2 == 0):
        return n == 2
    if (n % 3 == 0):
        return n == 3
    i = 5
    while i * i < n:
        if (n % i == 0):
            return False
        i += 1;
    return True

# 取出100以内的素数
print filter(is_prime, range(101)[1:])

def isnot_prime(n):
    return not is_prime(n)
# 删除100以内的素数
print filter(isnot_prime, range(101)[1:])
