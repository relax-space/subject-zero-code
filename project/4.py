'''
编写一个程序，从控制台接收一系列逗号分隔的数字，并生成一个列表和一个包含每个数字的元组。

假设向程序提供了以下输入：

34,67,55,33,12,98

那么，输出应该是：

['34'，'67'，'55'，'33'，'12'，'98']

('34','67','55','33','12','98')
'''


a = input('请输入一系列逗号分隔的数字：\n')
list = a.split(',')
tuple = tuple(list)

print(list)
print(tuple)