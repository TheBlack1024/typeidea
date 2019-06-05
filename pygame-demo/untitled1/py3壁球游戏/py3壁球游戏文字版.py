# Unit PYG03: Pygame Wall Ball Game version 5  伸缩型
import pygame, sys
import pygame.freetype

# 初始化变量
pygame.init()
size = width, height = 1200, 800
speed = [0, 0]
BLACK = 60, 8, 8
screen = pygame.display.set_mode(size, pygame.RESIZABLE)  # 窗口大小可调
# screen = pygame.display.set_mode(size, pygame.NOFRAME)  #窗口无边框
# screen = pygame.display.set_mode(size, pygame.FULLSCREEN)  #窗口全屏显示
GOLD = 255,251,0
RED = pygame.Color("red")
pos = (200,500)

# 初始化相关设置
pygame.display.set_caption("随便的汽车")
background = pygame.image.load("beijin.jpg")
ball = pygame.image.load("timg.gif")
pygame.display.set_icon(ball)
ballrect = ball.get_rect() # 矩形化ball对象
#ballrect = pos
print(ballrect)
fps = 300 # 屏幕刷新变量
fclock = pygame.time.Clock() # 屏幕刷新频率函数


# 字体和绘制字体 render_to方法-->rect
f1 = pygame.freetype.Font("C://Windows//Fonts//msyh.ttc",36)
f1rect = f1.render_to(screen,(200,300),"TanHeming",GOLD,RED,size =50)

# 字体绘制 render方法-->(Surface,rect)
f2surf,f2rect = f1.render("世界和平",fgcolor = RED)
#f2rect = pos

# 循环刷新事件和响应
while True:
    for event in pygame.event.get(): # 获取事件对比响应库
        if event.type == pygame.QUIT: # 窗口退出操作
            sys.exit()
        elif event.type == pygame.KEYDOWN: # 键盘输入
            if event.key == pygame.K_LEFT:
                #speed[0] = speed[0] - 1
                if ballrect.left < 0 :
                    pass
                else:
                    ballrect = ballrect.move(-10,0)
            elif event.key == pygame.K_RIGHT:
                #speed[0] = speed[0] + 1
                if ballrect.right > width :
                    pass
                else:
                    ballrect = ballrect.move(10, 0)
            elif event.key == pygame.K_UP:
                #speed[1] = speed[1] - 1
                if ballrect.top < 0 :
                    pass
                else:
                    ballrect = ballrect.move(0, -10)
            elif event.key == pygame.K_DOWN:
                #speed[1] = speed[1] + 1
                if ballrect.bottom > height:
                    pass
                else:
                    ballrect = ballrect.move(0, 10)
            elif event.key == pygame.K_ESCAPE:
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                #mouse_x -= 56
                #mouse_y -= 38
                ballrect = pos
                #ballrect = ballrect.move(event.pos[0]-ballrect.left,event.pos[1]-ballrect.top)

        elif event.type == pygame.VIDEORESIZE: # 伸缩窗口操作判断
            size = width, height = event.size[0], event.size[1] # 获取窗口伸缩的最新尺寸
            screen = pygame.display.set_mode(size, pygame.RESIZABLE) # 改变窗口尺寸
    #if pygame.display.get_active():# 感知程序是否最小化的函数使用
        #ballrect = ballrect.move(speed)
    #if ballrect.left < 0 or ballrect.right > width:
        #speed[0] = - speed[0]
    #if ballrect.top < 0 or ballrect.bottom > height:
        #speed[1] = - speed[1]

    # 刷新数据
    screen.fill(BLACK) # 刷新窗口绘制背景
    screen.blit(background,(0,0))

    f1rect = f1.render_to(screen, pos, "TanHeming", GOLD, RED, size=50)
    screen.blit(f2surf, f2rect)
    screen.blit(ball, ballrect)
    pygame.display.update() # 刷新数据
    fclock.tick(fps) # 屏幕刷新