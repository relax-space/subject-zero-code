'''
定义至少有两个方法的类：

get string：从控制台输入获取字符串

print string：以大写形式打印字符串。

也请包含简单的测试函数来测试类方法。
'''


def get()->str:
    a = input('请输入小写英文字符串：\n')
    return a

def print_str(raw:str):
    up =raw.upper()
    print(up)

def test():
    b = get()
    print_str(b)

test()