'''
写一个能计算给定 数的阶乘的程序。

结果应以逗号分隔的顺序打印在一行上。

例如： 5! = 1 * 2 * 3 * 4 * 5; 最后结果是 120

'''


def calc(n: int) -> int:
    if n > 1:
        return n * calc(n - 1)
    else:
        return 1


print(calc(5))
