
# coding=utf-8

if 0:
    from tkinter import *
    #创建根窗体
    root = Tk()
    #修整根窗体
    root.title("Robot GUI")
    root.geometry("300x200")


    # 在根窗体中创建一个框架，用它来承载其他的小部件
    app = Frame(root)
    app.grid()

    #在框架中创建一个标签
    lbl = Label(app,text = "I'm a label!")
    lbl.grid()

    #在框架中创建一个按钮
    bttn1 = Button(app,text = "nothing")
    bttn1.grid()

    #再创建一个按钮
    bttn2 = Button(app)
    bttn2.grid()
    bttn2.configure(text = "too")

    #再次创建一个按钮
    bttn3 = Button(app)
    bttn3.grid()
    bttn3["text"] = "Same here"

    #启动窗体事件循环
    root.mainloop()

# 使用类创建GUI
from tkinter import *

class Application(Frame):
    """A GUI application with three buttons"""

    def __init__(self,master):
        """Initialize the Frame"""
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # 在框架中创建一个按钮
        self.bttn1 = Button(self, text="nothing")
        self.bttn1.grid()

        # 再创建一个按钮
        self.bttn2 = Button(self)
        self.bttn2.grid()
        self.bttn2.configure(text="too")

        # 再次创建一个按钮
        self.bttn3 = Button(self)
        self.bttn3.grid()
        self.bttn3["text"] = "Same here"


def main():
    root = Tk()
    root.title("Robot GUI")
    root.geometry("500x300")

    app = Application(root)

    root.mainloop()

main()