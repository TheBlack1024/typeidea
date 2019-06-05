

# 全局变量和局部变量

a = 5 # 全局变量

def sum(a,b):
    x = a + b
    return x

y = sum(5,6)

print(a)
print(y)

# 内部作用域想修改外部作用域的变量
num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)
fun1()
print(num)
