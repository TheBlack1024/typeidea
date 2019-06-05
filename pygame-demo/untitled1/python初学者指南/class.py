
# coding=utf-8

#定义类
class Robot(object):
    """ The one robot"""
    total = 0#类特性

    #静态方法—类特性
    @staticmethod
    def status():
        print("The total number of critters is",Robot.total)

    #构造器
    def __init__(self,name,mood):
        print("a new robot has been born! ")
        self.name = name
        self.__mood = mood
        Robot.total += 1

    def __str__(self):# 直接打印对象时的方法
        rep = "The One Robot\n"
        rep += "name:" + self.name + "\n"
        rep += "mood:" + self.__mood + "\n"
        return rep
     #方法
    def takl(self):
        print("Hi! I'm ",self.name,"!")
        self.__private()

    #私有方法
    def __private(self):
        print("This is a private method!")

if 0:
    Robot.status()
    #实例化对象
    Robot1 = Robot("Aaron","good")#实例化了一个对象Robot1
    Robot2 = Robot("Bob","good")

    #调用方法
    Robot1.takl()
    print(Robot1)
    print(Robot2.name)

    Robot.status()
    print(Robot.total)


# 类的继承
class New_Robot(Robot):
    """Strong Robot"""
    def __init__(self,name,mood):#重写基类方法
        super(New_Robot, self).__init__(name,mood)#super函数保留原方法
        print("a new strong robot has been born!")

    def roar(self):
        print("I am very angry!")

robot1 = New_Robot("Tom","good")
robot1.roar()