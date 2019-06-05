# Unit PYG03: Pygame Wall Ball Game version 5  伸缩型
import pygame, sys

# 初始化变量
pygame.init()
size = width, height = 1000, 600
speed = [0, 0]
BLACK = 60, 8, 8
screen = pygame.display.set_mode(size, pygame.RESIZABLE)  # 窗口大小可调
# screen = pygame.display.set_mode(size, pygame.NOFRAME)  #窗口无边框
# screen = pygame.display.set_mode(size, pygame.FULLSCREEN)  #窗口全屏显示

# 初始化相关设置
pygame.display.set_caption("随便的汽车")
background = pygame.image.load("beijin.jpg")
ball = pygame.image.load("timg.gif")
pygame.display.set_icon(ball)
ballrect = ball.get_rect() # 矩形化ball对象
print(ballrect)
fps = 300 # 屏幕刷新变量
fclock = pygame.time.Clock() # 屏幕刷新频率函数

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
                    ballrect = ballrect.move(-100,0)
            elif event.key == pygame.K_RIGHT:
                #speed[0] = speed[0] + 1
                if ballrect.right > width :
                    pass
                else:
                    ballrect = ballrect.move(100, 0)
            elif event.key == pygame.K_UP:
                #speed[1] = speed[1] - 1
                if ballrect.top < 0 :
                    pass
                else:
                    ballrect = ballrect.move(0, -100)
            elif event.key == pygame.K_DOWN:
                #speed[1] = speed[1] + 1
                if ballrect.bottom > height:
                    pass
                else:
                    ballrect = ballrect.move(0, 100)
            elif event.key == pygame.K_ESCAPE:
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button ==1:
                #mouse_x,mouse_y = pygame.mouse.get_pos()
                #mouse_x -= 56
                #mouse_y -= 38
                #ballrect = (mouse_x,mouse_y)
                ballrect = ballrect.move(event.pos[0]-ballrect.left-(ballrect.right-ballrect.left)//2,event.pos[1]-ballrect.top-(ballrect.bottom-ballrect.top)//2)

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
    screen.blit(ball, ballrect)
    pygame.display.update() # 刷新数据
    fclock.tick(fps) # 屏幕刷新