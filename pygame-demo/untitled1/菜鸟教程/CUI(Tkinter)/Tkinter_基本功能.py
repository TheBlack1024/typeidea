
# coding=gbk
from tkinter import *
from win32api import GetSystemMetrics

top = Tk()
w = GetSystemMetrics(0)
h = GetSystemMetrics(1)
top.geometry("{0}x{1}".format(w,h))
b1 = Button(text="ɶ�����",bg ="red",padx=10,pady=5)
t1 = Entry(bg = "red",bd = 1)
top.title("С�����")


b1.pack()#���������봰��
b1.place(x=100,y=200)

t1.pack()
top.mainloop() #������Ϣѭ��