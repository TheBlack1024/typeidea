
#coding=utf-8

import pygame,sys
from random import *

#hero类
class Hero(object):
    """Hero class"""

    def __init__(self,pos):
        self.pos = pos
        self.name1 = pygame.image.load("Sprites/hero/fly/hero1.png").convert_alpha()
        self.name2 = pygame.image.load("Sprites/hero/fly/hero2.png").convert_alpha()
        self.hero_bullet = pygame.image.load("Sprites/bullet/fly/bullet2.png").convert_alpha()

        self.rect = self.name1.get_rect()
        self.rect = self.rect.move(self.pos)

        self.dealy ,self.dealy_key = 100,100
        self.dealy1,self.dealy1_key = 100,100

        self.hero_bullet_list = []#子弹库
        for i in range(100):
            self.hero_bullet_list.append(self.hero_bullet.get_rect())


    def control(self):
        """Hero control"""
        self.key_pressed = pygame.key.get_pressed()

        if self.key_pressed[pygame.K_LEFT]:
            if self.rect.left > -50:
                self.rect.left -= 2
            else:
                pass
        elif self.key_pressed[pygame.K_RIGHT]:
            if self.rect.right < 530:
                self.rect.right += 2
            else:
                pass
    def show(self, screen):
        """screen show"""
        if self.dealy % 2 == 0:
            screen.blit(self.name1,self.rect)
        elif self.dealy % 2 == 1:
            screen.blit(self.name2,self.rect)
        else:
            pass
        if self.dealy_key % 15 == 0:
            self.dealy -= 1
        else:
            pass
        self.dealy_key -= 1
        if self.dealy_key == 0:
            self.dealy_key = 100
        else:
            pass
        if self.dealy == 0:
            self.dealy = 100
        else:
            pass

        return self.rect

    def hero_bullte(self):
        """英雄子弹"""
        for i in range(100):
            screen.blit(self.hero_bullet,self.hero_bullet_list[i])

            self.hero_bullet_list[i] = self.hero_bullet_list[i].move([0,-10])

            if self.hero_bullet_list[i].top < -20:
                self.hero_bullet_list[i].center = self.rect.midtop
        return self.hero_bullet_list



class Enemy(object):
    """敌机类"""
    def __init__(self):
        self.enemy = pygame.image.load("Sprites/Enemy1/fly/enemy1.png").convert_alpha()
        self.bullet = pygame.image.load("Sprites/bullet/fly/bullet1.png").convert_alpha()

        self.enemy_rect_list = []#敌机rect对象列表
        self.enemy_speed_list = []#初始化敌机随机速列表
        self.bullet_rect_list = []  # 子弹rect对象列表
        for i in range(20):
            self.enemy_rect_list.append(self.enemy.get_rect())#初始化20个rect对象
            self.bullet_rect_list.append(self.bullet.get_rect())#初始化20个子弹rect对象

            self.enemy_pos = randint(10,430),randint(-3000,-5)#初始化20个位置
            self.enemy_rect_list[i] = self.enemy_rect_list[i].move(self.enemy_pos)

            self.enemy_speed_list.append([0,1])#初始化20个速度

    def E_motion(self,screen):
        """敌机自动化运动方法"""
        for i in range(5):

            screen.blit(self.bullet, self.bullet_rect_list[i])
            screen.blit(self.enemy, self.enemy_rect_list[i])

            if self.enemy_rect_list[i].top > 760:#判断敌机是否飞出画面
                self.enemy_rect_list[i] = self.enemy_rect_list[i].move(0,randint(-3000,-770))#回到机库
                self.enemy_speed_list[i] = [0,randint(1,2)]#重新获取速度
            else:
                self.enemy_rect_list[i] = self.enemy_rect_list[i].move(self.enemy_speed_list[i])#初始敌机速度


            if self.enemy_rect_list[i].top > 50:#子弹发射
                self.bullet_rect_list[i] = self.bullet_rect_list[i].move([self.enemy_speed_list[i][0], self.enemy_speed_list[i][1] + 1])
            else:
                self.bullet_rect_list[i].center = self.enemy_rect_list[i].center


        return  self.enemy_rect_list,self.bullet_rect_list



class Blast(object):
    """爆炸效果类"""
    def __init__(self):
        self.hero_blowup1 = pygame.image.load("Sprites/hero/down/hero_blowup_n1.png").convert_alpha()
        self.hero_blowup2 = pygame.image.load("Sprites/hero/down/hero_blowup_n2.png").convert_alpha()
        self.hero_blowup3 = pygame.image.load("Sprites/hero/down/hero_blowup_n3.png").convert_alpha()
        self.hero_blowup4 = pygame.image.load("Sprites/hero/down/hero_blowup_n4.png").convert_alpha()
        self.rect = self.hero_blowup1.get_rect()
        self.dealy = 100#动画哨兵
        self.dealy_key = 100#延时哨兵

        self.enemy_down1 = pygame.image.load("Sprites/Enemy1/down/enemy1_down1.png").convert_alpha()
        self.enemy_down2 = pygame.image.load("Sprites/Enemy1/down/enemy1_down2.png").convert_alpha()
        self.enemy_down3 = pygame.image.load("Sprites/Enemy1/down/enemy1_down3.png").convert_alpha()
        self.enemy_down4 = pygame.image.load("Sprites/Enemy1/down/enemy1_down4.png").convert_alpha()
        self.enemy_rect = self.enemy_down1.get_rect()
        self.enemy_dealy = 100#动画哨兵
        self.enemy_dealy_key = 100#延时哨兵

    def hero_blast(self,screen,rect):
        """hero爆炸效果方法"""
        self.rect = self.rect.clamp(rect)
        if self.dealy % 4 == 0:
            screen.blit(self.hero_blowup1,self.rect)
        elif self.dealy % 4 == 3:
            screen.blit(self.hero_blowup2,self.rect)
        elif self.dealy % 4 == 2:
            screen.blit(self.hero_blowup3,self.rect)
        else:
            screen.blit(self.hero_blowup4,self.rect)

        if self.dealy == 0:
            self.dealy = 100

        if not(self.dealy_key % 15):
            self.dealy -= 1

        self.dealy_key -= 1
        if self.dealy_key == 0:
            self.dealy_key = 100




    def enemy_blast(self,screen,rect):
        """敌机爆炸效果"""
        self.enemy_rect = self.enemy_rect.clamp(rect)
        if self.enemy_dealy % 4 == 0:
            screen.blit(self.enemy_down1,self.enemy_rect)
        elif self.enemy_dealy % 4 == 1:
            screen.blit(self.enemy_down2,self.enemy_rect)
        elif self.enemy_dealy % 4 == 2:
            screen.blit(self.enemy_down3,self.enemy_rect)
        else:
            screen.blit(self.enemy_down4,self.enemy_rect)

        if self.enemy_dealy == 0:
            self.enemy_dealy = 100
        else:
            if not(self.enemy_dealy_key % 15):
                self.enemy_dealy -= 1

        self.enemy_dealy_key -= 1
        if self.enemy_dealy_key == 0:
            self.enemy_dealy_key = 100







#创建主窗口函数
pygame.init()
#基础变量设置
size = width,height = 480,760
fps = 100
color = 255,255,255
speed = [0,0]
pos = 190,620
#导入图片
program_hero = pygame.image.load("Sprites/hero/fly/hero1.png")
background = pygame.image.load("images/background.png")

#设置窗口信息
screen = pygame.display.set_mode(size)
pygame.display.set_icon(program_hero)
pygame.display.set_caption("飞机大战")
#设置刷新时间函数
fclock = pygame.time.Clock()

#实例化一个对象

hero1 = Hero(pos)
enemy = Enemy()
b = Blast()
a = hero1.show(screen)



key = 1


# 设置循环
while True:
    #事件监听
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #数据上传和屏幕刷新
    screen.fill(color)
    screen.blit(background,(0,0))

    if key:
        c, d = enemy.E_motion(screen)
        e = hero1.hero_bullte()
        if a.collidelist(d) == -1 & a.collidelist(c) == -1:
            hero1.control()
            enemy.E_motion(screen)
            hero1.hero_bullte()
            hero1.show(screen)
            for i in c:
                if i.collidelist(e) != -1:
                    b.enemy_blast(screen,i)

        else:
            b.hero_blast(screen, a)
            key = 0





    pygame.display.update()
    fclock.tick(fps)

