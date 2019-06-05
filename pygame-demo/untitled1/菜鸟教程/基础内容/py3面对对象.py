
# 类的创建

class MyClass:
    """一个简单的类实例"""
    i = 12345
    def f(self):
        return 'hello world'

# 实例化类
x = MyClass()

# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())

print("-"*100)

# 创建一个类

class OK:
    """随便的一个类"""
    # 基本属性
    a = ("I love you!\n")
    i = 1  # 初始化的哨兵

    # 私有属性
    __t = "yes OK"

    def __init__(self): # 构造器方法
        print("构造器")
        print("hello word!")

    def P(self):
        while OK.i <= 2:
            for x in OK.a:
                print(x,end="")
            OK.i += 1

# 实例化类
b = OK()
print("="*100)
# 访问类属性和方法
b.P()
print("-"*100)
print(b.a) # 外部访问类属性
print(b._OK__t) # 外部访问私有类属性

print("="*100)
class people:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return '这个人的名字是%s,已经有%d岁了！'%(self.name,self.age)

a=people('孙悟空',999)
print(a)