# 屏幕绘制
import pygame, sys # 库调用
from math import pi

# 初始化变量
pygame.init()
size = width, height = 1200, 800
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption("pygame图形绘制")
GOLD = 255,251,0
RED = pygame.Color("red")

r1rect = pygame.draw.rect(screen,GOLD,(100,100,200,100),2)# 所绘屏幕，颜色，（x，y，宽，高），边框粗细度
r2rect = pygame.draw.rect(screen,RED,(100,300,200,100),2)
r3rect = pygame.draw.line(screen,GOLD,(300,500),(1000,600),2) # 绘制直线
r4rect = pygame.draw.ellipse(screen,RED,r1rect,2) # 绘制椭圆
r5rect = pygame.draw.arc(screen,GOLD,r2rect,0,pi/2,2) # 绘制椭线
r6rect = pygame.draw.circle(screen,RED,(500,500),100,0) # 绘制圆形
r7rect = pygame.draw.polygon(screen,GOLD,[(10,10),(10,110),(100,60)],2)# 绘制多边形
r8rect = pygame.draw.lines(screen,RED,False,[(520,100),(550,170),(570,160),(133,499),(400,588)],2) # 绘制多线
r9rect = pygame.draw.aaline(screen,GOLD,(600,400),(300,580),0) # 绘制无锯齿线
# 循环刷新事件和响应
while True:
    for event in pygame.event.get(): # 获取事件对比响应库
        if event.type == pygame.QUIT: # 窗口退出操作
            sys.exit()
    pygame.display.update()
