
# coding=utf-8

import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk

def main():

    root = Tk()
    root.title("大富贵电子点餐单")
    root.geometry("500x1000")
    #root.resizable(0,0)

    app = Application(root)

    root.mainloop()



class Application(Frame):

    def __init__(self,master):
        """Initialize Frame"""
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """大富贵菜单页面"""
        #抬头
        Label(self,
              text = "大富贵菜单",
              font = ("华文彩云",30)
              ).grid(row = 0,column = 1,columnspan = 2,sticky = W)
        if 1:
            # 凉菜文本
            Label(self,
                  text = "凉菜",
                  font = ("华文彩云",20),
                  ).grid(row = 2,column = 0,columnspan = 1,sticky = W)
            #凉菜字典
            self.liancai = {"lc_1": "花生米\t\t\t8元",
                       "lc_2": "黄瓜片\t\t\t8元",
                       "lc_3": "肉丝拉皮\t\t\t12元",
                       "lc_4": "姜汁松花蛋\t\t12元",
                       "lc_5": "虾皮包菜\t\t\t20元",
                       "lc_6": "老虎菜\t\t\t20元",
                       "lc_7": "麻酱豆角\t\t\t25元"
                       }
            num = 3
            # 凉菜复选框
            for lc in self.liancai:
                self.Lc = lc
                self.lc = BooleanVar()
                Checkbutton(self,
                            text=self.liancai[lc],
                            variable=self.lc,
                            command = self.update
                            ).grid(row = num,column = 0,columnspan = 1,sticky = W)
                num += 1
        if 1:
            # 素菜文本
            Label(self,
                  text = "素菜",
                  font = ("华文彩云",20),
                  ).grid(row = 3 + len(self.liancai),column = 0,columnspan = 1,sticky = W)
            #素材菜字典
            sucai = {"sc_1": "家常豆腐\t\t\t12元",
                       "sc_2": "西红柿鸡蛋\t\t10元",
                       "sc_3": "地三鲜\t\t\t8元",
                       "sc_4": "辣子豆皮\t\t\t8元",
                       "sc_5": "老匠白菜\t\t\t12元",
                       "sc_6": "韭香木耳\t\t\t8元",
                       "sc_7": "山芹炒肉\t\t\t12元",
                     "sc_8": "麻辣豆腐\t\t\t12元",
                     "sc_9": "红烧茄子\t\t\t8元",
                     "sc_10": "酸辣土豆丝\t\t4元",
                     "sc_11": "醋溜山药\t\t\t8元",
                     "sc_12": "炸蘑菇\t\t\t8元",
                     "sc_13": "尖椒鸡蛋\t\t\t10元",
                       }
            num = 4 + len(self.liancai)
            # 素菜复选框
            for sc in sucai:
                self.sc = BooleanVar()
                Checkbutton(self,
                            text=sucai[sc],
                            variable=self.sc,
                            ).grid(row = num,column = 0,columnspan = 2,sticky = W)
                num += 1

        if 1:
            # 荤菜文本
            Label(self,
                  text = "荤菜",
                  font = ("华文彩云",20),
                  ).grid(row = 2,column = 2,columnspan = 1,sticky = W)
            #荤材菜字典
            huncai = {"hc_1": "家常豆腐\t\t\t12元",
                       "hc_2": "西红柿鸡蛋\t\t10元",
                       "hc_3": "地三鲜\t\t\t8元",
                       "hc_4": "辣子豆皮\t\t\t8元",
                       "hc_5": "老匠白菜\t\t\t12元",
                       "hc_6": "韭香木耳\t\t\t8元",
                       "hc_7": "山芹炒肉\t\t\t12元",
                     "hc_8": "麻辣豆腐\t\t\t12元",
                     "hc_9": "红烧茄子\t\t\t8元",
                     "hc_10": "酸辣土豆丝\t\t4元",
                     "hc_11": "醋溜山药\t\t\t8元",
                     "hc_12": "炸蘑菇\t\t\t8元",
                     "hc_13": "尖椒鸡蛋\t\t\t10元",
                       }
            num = 3
            # 荤菜复选框
            for hc in huncai:
                self.hc = BooleanVar()
                Checkbutton(self,
                            text=huncai[hc],
                            variable=self.hc,
                            ).grid(row = num,column = 2,columnspan = 1,sticky = W)
                num += 1

        if 1:
            Button(self,
                   text = "提交菜单",
                   #command = self.update_txt
                   ).grid(row = 4 + len(huncai),column = 2,sticky = W)
            self.zongjia_txt = Text(self,width = 30,height = 5,wrap = WORD)
            self.zongjia_txt.grid(row = 6 + len(huncai),column = 2,sticky = W)



        Label(self,
              text = "备注：",
              font = ("花纹云彩",20)
              ).grid(row = 29,column = 0,sticky = W)
        self.kuan_txt = Text(self,width = 70,height =10,wrap = WORD)
        self.kuan_txt.grid(row =30,column = 0,columnspan = 3,sticky = W)


    def update(self):
        """款选数据上传"""
        LC = self.Lc
        print(LC)





main()