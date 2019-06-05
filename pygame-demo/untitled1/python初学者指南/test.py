
# coding=utf-8
if 0:
    def tipper(tipper):
        a = tipper * 0.15
        b = tipper * 0.2
        c = tipper + a
        print("15%:",a)
        print("20%:",b)
        print("您需要支付的总金额为：",c)

    c = int(input("请输入您的餐费："))
    tipper(c)

if 0:
    a = "conversatinon"
    for i in range(1,10,2):
        print(i,end=" ")
    print()
    print(len(a))
    print("a" in a)
if 0:
    fundamental = ('sword',
                   'armor',
                   'shiela',
                   'healing potion')
    perspective = ('哈哈','嘻嘻','呵呵')
    print(fundamental + perspective)
    #for i in fundamental:
        #print(i)

if 0:
    a = input("亲输入一句话：")
    for i in  range(len(a)):
        print(a[-i-1],end=" ")

if 0:
    a = {'1':'a','2':'b','3':'c','4':'5'}
    print(a.keys())
    print(a.values())
    print(a.items())


if 0:
    import random
    a = ["book","loud","love","plate"]

    for x in range(len(a)):
        i = random.randrange(len(a))
        print(a[i])
        del a[i]

if 0:
    with open("test.txt","a") as f:
        #for line in f:
            #print(line,end="")
        b = ("忆北岁",
             "\n从容自若入门去，",
             "\n归来依旧少年人。",
             "\n回首再忆飘零日，",
             "\n皆是美酒醉幽魂。\n")
        f.writelines(b)

if 0:
    import pickle,shelve
    with open("test.dat","rb") as f:
        #for line in f:
            #print(line,end="")
        b = ("忆北岁",
             "\n从容自若入门去，",
             "\n归来依旧少年人。",
             "\n回首再忆飘零日，",
             "\n皆是美酒醉幽魂。\n")
        c = pickle.load(f)
        d = pickle.load(f)
        print(c)
        print(d)


if 0:
    import pickle,shelve
    with shelve.open("test2","c") as f:
        b = ["忆北岁",
             "\n从容自若入门去，",
             "\n归来依旧少年人。",
             "\n回首再忆飘零日，",
             "\n皆是美酒醉幽魂。"]
        f["忆北岁"] = b
        f.sync()
        print(f["忆北岁"])



if 0:
    # coding=utf-8

    from tkinter import *
    from PIL import *



    def main():
        root = Tk()
        root.title("大富贵电子点餐单")
        root.geometry("500x800")
        #root.resizable(0,0)

        #photo = PhotoImage(file = "BG.jpg")
        #Label(root,
              #image = photo
              #).place(x = 0,y = 0)

        app = Application(root)

        root.mainloop()


    class Application(Frame):

        def __init__(self, master):
            """Initialize Frame"""
            super(Application, self).__init__(master)
            self.grid()
            self.create_widgets()

        def create_widgets(self):
            """大富贵菜单页面"""
            # 抬头
            self.photo = PhotoImage(file="BG.jpg")
            Label(self,
                  text="大富贵菜单",
                  #background = "red",
                  foreground = "red",
                  font = ("微软雅黑",20),
                  #compound = "center",
                  #image = self.photo
                  ).grid(row = 0,column = 0,sticky = W)

            # 凉菜文本
            #Label(self,
                  #text="凉菜",
                  #background = "red"
                  #).grid(row=3, column=0, sticky=W)
            self.txt = Text(self,
                            width = 30,height = 10,
                            wrap = WORD)
            self.txt.grid(row = 2,column = 2,columnspan = 2,sticky = W)
            self.buttn = Button(self,
                            text = "点击输入",
                            command = self.update
                             ).grid(row = 3,column = 3)

        def update(self):
            """点击输入"""
            likes = "conversation"

            self.txt.delete(0.0,END)
            self.txt.insert(0.0,likes)



    main()



if 0:
    import pygame

    class Hero(object):
        """Hero class"""
        def __init__(self,name,address,pos):
            self.name,self.address,self.pos = name,address,pos
            self.name = pygame.image.load(self.address)
            self.rect = self.name.get_rect()
            self.rect = self.rect.move(self.pos)

        def control(self,event):
            """Hero control"""
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.rect = self.rect.move(-10, 0)
                elif event.key == pygame.K_RIGHT:
                    self.rect = self.rect.move(10, 0)
                else:
                    pass
            else:
                pass

        def show(self,screen):
            """screen show"""
            screen.blit(self.name,self.rect)

if 1:

    import pygame,sys,time

    pygame.init()

    size = width,height = 500,700
    color = 255,255,255
    fsp = 60
    speed = [0,0]
    pos = 0,0

    image = pygame.image.load("Sprites/hero/fly/hero1.png")
    image1 = pygame.image.load("Sprites/hero/down/hero_blowup_n1.png")
    image2 = pygame.image.load("Sprites/hero/down/hero_blowup_n2.png")
    image3 = pygame.image.load("Sprites/hero/down/hero_blowup_n3.png")
    image4 = pygame.image.load("Sprites/hero/down/hero_blowup_n4.png")

    bullet = pygame.image.load("Sprites/bullet/fly/bullet1.png")

    hero_down = image1.get_rect()
    bullet_rect = bullet.get_rect()


    hero_down.center = 220,600
    bullet_rect.center = hero_down.center
    image_list = []
    image_list.append(image1)
    image_list.append(image2)
    image_list.append(image3)
    image_list.append(image4)





    screen = pygame.display.set_mode(size,pygame.RESIZABLE)
    pygame.display.set_caption("飞机大战")
    pygame.display.set_icon(image)

    fclock = pygame.time.Clock()

    convert_key = True
    dealy = 100
    dealy_key = 100

    while True:
        screen.fill(color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        key_pressed = pygame.key.get_pressed()

        if key_pressed[pygame.K_UP]:
            hero_down.top -= 10


        screen.blit(bullet,bullet_rect)
        screen.blit(image, hero_down)
        screen.blit(image1,(200,200))




        pygame.display.flip()
        fclock.tick(60)


    if 0:
        for i in range(0,10):
            if enemy_list[i].top > 760:
                speed_list[i] = [0, randrange(1, 3)]
            else:
                pass
            enemy_list[i] = enemy_list[i].move(speed_list[i])
            if enemy_list[i].top > 0:
                bullet_speed = speed_list[i][0],speed_list[i][1]+1
                bullet_list[i] = bullet_list[i].move(bullet_speed)
            else:
                bullet_list[i] = bullet_list[i].clamp(enemy_list[i])
            screen.blit(bullet,bullet_list[i])
            screen.blit(little_fly, enemy_list[i])

    if 0:
        # rect化图片对象

        # 设置敌机list
        enemy_list = []
        for i in range(0, 20):
            enemy_list.append("enemy" + str(i))
            enemy_list[i] = little_fly.get_rect()

        # 敌机随机速度list
        speed_list = []
        for i in range(0, 20):
            speed_list.append([0, randrange(1, 3)])

        # 敌机随机位置
        for i in range(0, 20):
            enemy_pos = randint(10, 430), randint(-1000, -5)
            enemy_list[i] = enemy_list[i].move(enemy_pos)

        # 敌机子弹了list
        bullet_list = []
        for i in range(0, 1000):
            bullet_list.append("bullet" + str(i))
            bullet_list[i] = bullet.get_rect()

        # 敌机子弹库
        for i in range(0, 1000):
            bullet_pos = -10, -10
            bullet_list[i] = bullet_list[i].move(bullet_pos)

        for i in range(0, 20):
            bullet_list[i] = bullet_list[i].clamp(enemy_list[i])
            bullet_list[i] = bullet_list[i].move(28, 22)





















