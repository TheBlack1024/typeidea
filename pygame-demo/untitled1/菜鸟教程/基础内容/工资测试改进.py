# 工资测试

an = ("你确定不要工资?",
      "不用面试了，直接来上班吧!",
      "挺好的！过来面试吧!",
      "有点高！不过还能接受，那明天来面试吧!",
      "你不适合我们，祝你好运!"
      )  # 元组

i = ""  # 初始化哨兵
while i != "n" and i != "N":
    try:
        a = int(input("\n请输入你想的工资："))  # 获取用户输入
        if a <= 0:
            print(an[0])

        elif 0 < a <= 2500:
            print(an[1])

        elif 2500 < a <= 6500:
            print(an[2])

        elif 6500 < a <= 10000:
            print(an[3])

        else:
            print(an[4])

        i = input("\n是否继续输入工资测试（y/n）：")

        while i != "y" and i != "Y" and i != "n" and i != "N":
            i = input("\n输入不正确，是否继续输入工资测试（y/n）：")

    except ValueError:
        print("\n输入不是有效数值")

input("\n按任意键测试游戏结束！")