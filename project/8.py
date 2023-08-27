'''
编写一个程序，接受以逗号分隔的单词序列作为输入，并在按字母顺序排序后以逗号分隔的序列打印单词。

假设向程序提供了以下输入：

without,hello,bag,world

那么，输出应该是：

bag,hello,without,world
'''

a = input('请输入单词：\n')
list = a.split(',')
list.sort()

print(','.join(list))