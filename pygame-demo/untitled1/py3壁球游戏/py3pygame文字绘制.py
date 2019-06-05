# 文字绘制
import pygame, sys
import pygame.freetype



# 初始化变量
pygame.init()
size = width, height = 1200, 800
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption("pygame文字绘制")
GOLD = 255,251,0
RED = pygame.Color("red")

# 字体和绘制字体 render_to方法-->rect
f1 = pygame.freetype.Font("C://Windows//Fonts//msyh.ttc",36)
f1rect = f1.render_to(screen,(200,300),"TanHeming",GOLD,RED,size =50)

# 字体绘制 render方法-->(Surface,rect)
f2surf,f2rect = f1.render("世界和平",fgcolor = RED)



# 循环刷新事件和响应
while True:
    for event in pygame.event.get(): # 获取事件对比响应库
        if event.type == pygame.QUIT: # 窗口退出操作
            sys.exit()

    screen.blit(f2surf,(323,456))
    pygame.display.update()
