
# coding=utf-8
# GUI部件布局管理器

from tkinter import *

class Application(Frame):
    """GUI application which can reveal the secret of longevity."""
    def __init__(self,master):
        """Initialize the frame."""
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Create button, text, and entry widgets."""
        #创建用于说明的标签,用Label
        self.inst_lbl = Label(self,text = "Enter password for the secret of longevity.")
        self.inst_lbl.grid(row = 0,column = 0,columnspan = 2,sticky = W)

        #创建密码文案提示词
        self.pw_lbl = Label(self,text = "Password:")
        self.pw_lbl.grid(row = 1,column = 0, sticky = W)

        #创建密码输入单行文本输入框，用Entry
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row = 1,column = 1,sticky = W)

        #创建密码提交请求按钮，用Button
        self.submit_bttn = Button(self,text = "Sumbit",command = self.reveal)
        self.submit_bttn.grid(row = 2,column = 0,sticky = W)

        #创建用于显示消息的Text小部件
        self.secret_txt = Text(self,width = 35, height = 5,wrap = WORD)
        self.secret_txt.grid(row = 4,column = 0,columnspan = 2,sticky = W)

        #创建复选框,用BooleanVar,Checkbutton
        #Comdey框
        self.likes_comedy = BooleanVar()#先实例化一个BooleanVar对象
        Checkbutton(self,
                    text = "Comedy",
                    variable = self.likes_comedy,
                    command = self.update_text
                    ).grid(row = 6,column = 0, sticky = W)

        # Drama框
        self.likes_drama = BooleanVar()  # 先实例化一个BooleanVar对象
        Checkbutton(self,
                    text="Drama",
                    variable=self.likes_drama,
                    command =self.update_text
                    ).grid(row=7, column=0, sticky=W)

        # Romance框
        self.likes_romance = BooleanVar()  # 先实例化一个BooleanVar对象
        Checkbutton(self,
                    text="Comedy",
                    variable=self.likes_romance,
                    command=self.update_text
                    ).grid(row=8, column=0, sticky=W)
        # 创建复选框状态结果的文本显示框
        self.results_txt = Text(self,width = 40, height = 5,wrap = WORD)
        self.results_txt.grid(row = 10,column = 0,columnspan = 3)

        # 创建单选框，用StringVar,Radiobutton
        self.favorite = StringVar()
        self.favorite.set(None)

        #创建Comedy框
        Radiobutton(self,
                    text = "comedy",
                    variable = self.favorite,
                    value = "comedy",
                    command = self.update_text1
                    ).grid(row = 14,column = 0,sticky = W)

        #创建Drama框
        Radiobutton(self,
                    text = "drama",
                    variable = self.favorite,
                    value = "drama",
                    command = self.update_text1
                    ).grid(row = 15,column = 0,sticky = W)

        #创建Romance框
        Radiobutton(self,
                    text = "romance",
                    variable = self.favorite,
                    value = "romance",
                    command = self.update_text1
                    ).grid(row = 16,column = 0,sticky = W)
        #创建显示结果的文本框
        self.results_txt1 = Text(self,width = 40, height = 5,wrap = WORD)
        self.results_txt1.grid(row = 17,column = 0,columnspan = 3)



    def update_text(self):
        """Update text widget and display user's favorite movie types."""
        likes = ""

        if self.likes_comedy.get():
            likes += "You like comedic movies.\n"

        if self.likes_drama.get():
            likes += "You like drama movies.\n"

        if self.likes_romance.get():
            likes += "You like romance movies."

        self.results_txt.delete(0.0,END)
        self.results_txt.insert(0.0,likes)

    def update_text1(self):
        """Update text widget and display user's favorite movie types."""
        message = "You favorite type of movie is "
        message += self.favorite.get()
        print(self.favorite.get())

        self.results_txt1.delete(0.0,END)
        self.results_txt1.insert(0.0,message)

    def reveal(self):
        """"Display message based on password."""
        contents = self.pw_ent.get()
        if contents == "secret":
            message = "Here's the secret to living to 100: live to 99 "\
                      "and then be VERY careful."
        else:
            message = "That's not the correct password ,so I can't share "\
                      "the secret whit you."
        self.secret_txt.delete(0.0,END)
        self.secret_txt.insert(0.0,message)







def main():
    root = Tk()
    root.title("GUI布局管理器")
    root.geometry("1000x800")

    app = Application(root)

    root.mainloop()


main()