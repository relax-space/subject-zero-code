'''
编写一个以2位X，Y为输入，生成二维数组的程序。数组的第i行和第j列中的元素值应为i*j。

注：i=0,1…，X-1；j=0,1，…Y-1。

例子

假设程序有以下输入：

3,5

那么，程序的输出应该是：

[[0，0，0，0，0]，
[0，1，2，3，4]，
[0，2，4，6，8]]

'''


def calc(x: int, y: int) -> list:
    arr = [[0 for i in range(y)] for j in range(x)]
    for i in range(x):
        for j in range(y):
            arr[i][j] = i * j
    return arr


def calc1(x: int, y: int) -> list:
    arr = [[i * j for i in range(y)] for j in range(x)]
    return arr


print(calc1(3, 5))
