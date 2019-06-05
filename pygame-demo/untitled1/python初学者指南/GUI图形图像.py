
# coding=utf-8
#创建图形窗口

import pygame,sys


pygame.init()
size = width,height = 480,760
fps = 24
pos = 210,600
color = 255,255,255
speed = [0,0]
icon = pygame.image.load("Sprites/hero/fly/hero1.png")
background = pygame.image.load("images/background.png")

screen = pygame.display.set_mode(size,pygame.RESIZABLE)
pygame.display.set_caption("飞机大战")
pygame.display.set_icon(icon)
fclock = pygame.time.Clock()

position = icon.get_rect()
position = position.move(200,600)
#position = pos



while True:
    for event in pygame.event.get(): # 获取事件对比响应库
        if event.type == pygame.QUIT: # 窗口退出操作
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if position.left < 0:
                    pass
                else:
                    speed[0] -= 1

            elif event.key == pygame.K_RIGHT:
                if position.right > width:
                    pass
                else:
                    speed[0] += 1

            elif event.key == pygame.K_ESCAPE:
                sys.exit()


        elif event.type == pygame.VIDEORESIZE: # 伸缩窗口操作判断
            size = width, height = event.size[0], event.size[1] # 获取窗口伸缩的最新尺寸
            screen = pygame.display.set_mode(size, pygame.RESIZABLE) # 改变窗口尺寸
    if position.left < 0 or position.right > width:
        speed[0],speed[1] = -speed[0],-speed[1]
    else:
        pass
    position = position.move(speed)
    screen.fill(color)
    screen.blit(background, (0, 0))
    screen.blit(icon,position)
    pygame.display.update()
    fclock.tick(fps)


