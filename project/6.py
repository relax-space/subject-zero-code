'''
编写一个程序，根据给定的公式计算并打印值：

Q= [(2 * C * D)/H]的平方根

C和H的固定值如下：

C是50。H是30。

D是一个变量，其值应以逗号分隔的顺序输入到程序中。

例子

假设程序有以下逗号分隔的输入序列：

100,150,180

程序的输出应为：

18，22，24
'''

import math


def calc(D: int) -> int:
    C = 50
    H = 30
    v = (2 * C * D) / H
    return int(math.sqrt(v))


a = input('请输入逗号分隔的序列：\n')
list = a.split(",")
res_str = ''
for s in list:
    i = int(s)
    res_str += f',{calc(i)}'

print(res_str[1:])
